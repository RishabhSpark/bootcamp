import requests
from typing import Optional, Dict, Any, List
from xml.etree import ElementTree as ET
from src.models.FigureData import FigureData
from src.models.PaperData import PaperData
from src.ingestion.entity_fetcher import extract_entities_pubtator3
from src.utils.logger import get_logger
from src.config.config_loader import load_config

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
    """Extract figure captions from the BioC XML root."""
    figures: List[Dict[str, Any]] = []
    
    for passage in root.iter("passage"):
        section_type: Optional[str] = None
        passage_type: Optional[str] = None
        figure_name: Optional[str] = None
        
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
            if caption and figure_name:
                logger.info(f"Figure found: {figure_name.strip()}")
                entities = extract_entities_pubtator3(caption.strip())
                figures.append(FigureData(
                    figure_name=figure_name.strip(),
                    figure_caption=caption.strip(),
                    entities=[]
                ))
                
    logger.info(f"Total figures found: {len(figures)}")
    return figures

def fetch_paper(pmc_id: str) -> PaperData:
    """
    Fetch paper info and figure captions from BioC-PMC API.
    Returns PaperData with title, abstract, and list of figures.
    """
    url = f"https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_xml/{pmc_id}/unicode"

    try:
        logger.info(f"Requesting BioC data for PMC {pmc_id}")
        response = requests.get(url, timeout=10, headers={"Accept": "application/xml"})
        
        if response.status_code != 200:
            logger.warning(f"BioC API returned status {response.status_code} for {pmc_id}")
            raise ValueError(f"BioC API error {response.status_code} for {pmc_id}")
        
        content = response.text.strip()
        if not content or not content.startswith('<?xml'):
            logger.warning(f"Received invalid or non-XML content for {pmc_id}")
            if content.startswith('<!DOCTYPE html') or '<html' in content.lower():
                logger.debug(f"Received HTML instead of XML: {content[:200]}")
            else:
                logger.debug(f"Response content (snippet): {content[:200]}")
            raise ValueError(f"Invalid XML response for {pmc_id}")


        try:
            root = ET.fromstring(content)

            title = extract_title(root)
            abstract = extract_abstract(root)
            figures = extract_figures(root)

            logger.info(f'Paper data extracted successfully for PMC {pmc_id}')
            return PaperData(pmcid = pmc_id, title=title, abstract=abstract, figures=figures)
        
        except ET.ParseError as e:
            logger.error(f"Error parsing XML for {pmc_id}: {e}")
            raise ValueError(f"XML parsing error for {pmc_id}: {e}") 

    except Exception as e:
        logger.error(f"Error fetching BioC paper {pmc_id}: {e}", exc_info=True)
        raise