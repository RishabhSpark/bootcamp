import requests
from typing import Optional, List
from xml.etree import ElementTree as ET
from src.models.FigureData import FigureData
from src.models.PaperData import PaperData
from src.utils.logger import get_logger
from src.config.config_loader import load_config
from src.ingestion.pmcid_to_pmid import pmcid_to_pmid

config = load_config()
logger = get_logger(__name__, level=config.log_level, log_to_file=config.log_to_file, log_file_path=config.log_file_path)

def extract_title(root: ET.Element) -> Optional[str]:
    """Extract the paper title from the BioC XML root."""
    logger.debug("Extracting title from BioC XML")
    for passage in root.findall(".//passage"):
        infons = {infon.get("key"): infon.text for infon in passage.findall("infon")}
        if infons.get("type") == "front":
            text = passage.findtext("text")
            if text:
                logger.info(f"Title found: {text.strip()}")
                return text.strip()
    logger.warning("Title not found in BioC XML")
    return None

def extract_abstract(root: ET.Element) -> str:
    """Extract the abstract text from the BioC XML root."""
    logger.debug("Extracting abstract from BioC XML")
    for passage in root.iter("passage"):
        section_type: Optional[str] = None
        passage_type: Optional[str] = None

        for infon in passage.findall("infon"):
            if infon.attrib.get("key") == "section_type":
                section_type = infon.text
            elif infon.attrib.get("key") == "type":
                passage_type = infon.text

        if (section_type and section_type.upper() == "ABSTRACT") or (passage_type and passage_type.lower() == "abstract"):
            text_elem = passage.find("text")
            if text_elem is not None:
                logger.info("Abstract found")
                return text_elem.text.strip()
    logger.warning("Abstract not found in BioC XML")
    return ""

def extract_figures(root: ET.Element) -> List[FigureData]:
    """Extract figure captions and their entities from BioC XML root."""
    figures: List[FigureData] = []

    for passage in root.iter("passage"):
        section_type = passage_type = figure_name = None

        for infon in passage.findall("infon"):
            key = infon.attrib.get("key")
            if key == "section_type":
                section_type = infon.text
            elif key == "type":
                passage_type = infon.text
            elif key == "file":
                figure_name = infon.text

        if (section_type == "FIG") and (passage_type == "fig_caption"):
            caption = passage.findtext("text")
            if not caption or not figure_name:
                continue

            # Parse entities
            entities = []
            for annotation in passage.findall("annotation"):
                ent_type = None
                ent_id = None
                ent_text = annotation.findtext("text")

                for infon in annotation.findall("infon"):
                    key = infon.attrib.get("key")
                    if key == "type":
                        ent_type = infon.text
                    elif key == "identifier":
                        ent_id = infon.text

                if ent_text and ent_type:
                    entities.append({
                        "text": ent_text,
                        "type": ent_type,
                        "id": ent_id or "",
                    })

            logger.info(f"Figure found: {figure_name.strip()} with {len(entities)} entities.")
            figures.append(FigureData(
                figure_name=figure_name.strip(),
                figure_caption=caption.strip(),
                entities=entities
            ))

    logger.info(f"Total figures found: {len(figures)}")
    return figures

def fetch_paper(pmc_id: str) -> PaperData:
    """
    Fetch paper info and figure captions using BioC PMC for title/abstract and PubTator for figures.
    """
    # Fetch and parse title/abstract from PMC BioC API
    url_pmc = f"https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/{pmc_id}/unicode"
    try:
        logger.info(f"Requesting BioC PMC data for PMC {pmc_id}")
        response = requests.get(url_pmc, timeout=10, headers={"Accept": "application/xml"})
        if response.status_code != 200:
            raise ValueError(f"BioC PMC API error {response.status_code} for {pmc_id}")
        
        content = response.text.strip()
        if not content.startswith('<?xml'):
            raise ValueError(f"Invalid XML response from PMC for {pmc_id}")
        
        root = ET.fromstring(content)
        title = extract_title(root) or "No title found"
        abstract = extract_abstract(root) or "No abstract found"
    
    except Exception as e:
        logger.error(f"Failed to fetch PMC title/abstract: {e}", exc_info=True)
        raise

    # Fetch and parse figures from PubTator BioC API
    try:
        try:
            pmid = pmcid_to_pmid(pmcid=pmc_id)
        except Exception as e:
            logger.warning(f"Could not map PMC {pmc_id} to PMID: {e}")
            pmid = None
    
        url_pubtator = f"https://www.ncbi.nlm.nih.gov/research/pubtator3-api/publications/export/biocxml?pmids={pmid}&full=true"
        logger.info(f"Requesting PubTator data for PMID {pmid}")
        response_fig = requests.get(url_pubtator, timeout=10)

        if response_fig.status_code != 200:
            raise ValueError(f"PubTator API error {response_fig.status_code} for PMID {pmid}")

        fig_root = ET.fromstring(response_fig.content)
        figures = extract_figures(fig_root)

    except Exception as e:
        logger.warning(f"Failed to fetch figures from PubTator for PMC {pmc_id}: {e}", exc_info=True)
        figures = []  # fallback to empty list if PubTator fails

    return PaperData(
        pmcid=pmc_id,
        title=title,
        abstract=abstract,
        figures=figures
    )