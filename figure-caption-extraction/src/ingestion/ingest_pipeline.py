from typing import List
from src.models.PaperData import PaperData
from src.ingestion.bioc_fetcher import fetch_paper
from src.utils.logger import get_logger
from src.config.config_loader import load_config

config = load_config()
logger = get_logger(__name__, level=config.log_level, log_to_file=config.log_to_file, log_file_path=config.log_file_path)

def ingest_pmc_ids(pmc_ids: List[str]) -> List[PaperData]:
    papers = []

    for pmc_id in pmc_ids:
        logger.info(f"Processing PMC ID: {pmc_id}")
        try:
            paper = fetch_paper(pmc_id)
            papers.append(paper)
            logger.info(f"Successfully processed PMC ID: {pmc_id}")
        except Exception as e:
            logger.warning(f"Skipping PMC {pmc_id} due to error: {e}")
            continue

    logger.info(f"Total papers processed: {len(papers)}")
    return papers