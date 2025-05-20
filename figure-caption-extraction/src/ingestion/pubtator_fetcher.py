import requests
from typing import List
import os
from src.models.FigureData import Entity
from src.ingestion.pmcid_to_pmid import pmcid_to_pmid
from src.utils.logger import get_logger
from src.config.config_loader import load_config
from dotenv import load_dotenv

load_dotenv()
config = load_config()
logger = get_logger(__name__, level=config.log_level, log_to_file=config.log_to_file, log_file_path=config.log_file_path)


def fetch_entities_pubtator(pmcid: str) -> List[Entity]:
    """
    Fetch entities from PubTator for a PMC ID.
    """
    base_url = "https://www.ncbi.nlm.nih.gov/research/pubtator3-api/publications/export/pubtator"

    pmid = pmcid_to_pmid(pmcid)

    url = f"{base_url}?pmids={pmid}"

    logger.info(f"Fetching PubTator entities for PMCID: {pmcid} via URL: {url}")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        content = response.text.strip()

        if not content:
            logger.warning(f"Empty response from PubTator for ID: {pmcid}")
            return []

    except Exception as e:
        logger.error(f"Error fetching PubTator data for {pmcid}: {e}", exc_info=True)
        return []

    entities: List[Entity] = []
    for line in content.split("\n"):
        if "|" in line or line.startswith("#"):
            continue  # skip metadata lines

        parts = line.split("\t")
        if len(parts) < 6:
            logger.debug(f"Skipping malformed line: {line}")
            continue

        try:
            start, end = int(parts[1]), int(parts[2])
            mention, entity_type = parts[3], parts[4]
            logger.debug(f"Parsed entity: {mention} ({entity_type}) [{start}-{end}]")
            entities.append(Entity(text=mention, type=entity_type, start=start, end=end))
        except Exception as e:
            logger.warning(f"Failed to parse line: {line} - {e}")
            continue

    logger.info(f"Total entities extracted for {pmcid} [pmid {pmid}]: {len(entities)}")
    return entities


def fetch_entities_from_text(text: str) -> List[Entity]:
    """
    Fetch biomedical entities from PubTator using free-text input.
    """
    url = "https://www.ncbi.nlm.nih.gov/research/publications/export/format?pmids=pmids"
    headers = {
        "Content-Type": "text/plain",
        "Accept": "text/tab-separated-values"
    }

    logger.info("Sending custom text to PubTator for annotation.")

    try:
        response = requests.post(url, headers=headers, data=text.encode("utf-8"), timeout=10)
        response.raise_for_status()
        content = response.text.strip()

        if not content:
            logger.warning("PubTator returned empty response for custom text.")
            return []

    except Exception as e:
        logger.error(f"Error fetching PubTator annotations for text: {e}", exc_info=True)
        return []

    entities: List[Entity] = []
    for line in content.split("\n"):
        if "|" in line or line.startswith("#"):
            continue  # skip metadata lines

        parts = line.split("\t")
        if len(parts) < 6:
            logger.debug(f"Skipping malformed line: {line}")
            continue

        try:
            start, end = int(parts[1]), int(parts[2])
            mention, entity_type = parts[3], parts[4]
            entities.append(Entity(text=mention, type=entity_type, start=start, end=end))
        except Exception as e:
            logger.warning(f"Failed to parse line: {line} - {e}")
            continue

    logger.info(f"Total entities extracted from custom text: {len(entities)}")
    return entities