import requests
from typing import Optional
from src.utils.logger import get_logger
from src.config.config_loader import load_config

config = load_config()
logger = get_logger(__name__, level=config.log_level, log_to_file=config.log_to_file, log_file_path=config.log_file_path)

def pmcid_to_pmid(pmcid: str) -> Optional[str]:
    """
    Convert a PMCID to a PMID using the NCBI ID Converter API.
    """
    url = f"https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/?tool=PubPaperCopilot&email=example@example.com&ids={pmcid}&format=json"
    logger.info(f"Converting PMCID to PMID using: {url}")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        records = data.get("records", [])
        if not records or "pmid" not in records[0]:
            logger.warning(f"No PMID found for PMCID: {pmcid}")
            return None

        pmid = records[0]["pmid"]
        logger.info(f"Found PMID {pmid} for PMCID {pmcid}")
        return pmid

    except Exception as e:
        logger.error(f"Failed to convert PMCID {pmcid} to PMID: {e}", exc_info=True)
        return None
    
    