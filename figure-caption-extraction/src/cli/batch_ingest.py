import os
import csv
import json
import typer
from typing import List
from src.ingestion.ingest_pipeline import ingest_pmc_ids
from src.storage.duckdb_writer import DuckDBWriter
from src.utils.logger import get_logger
from src.config.config_loader import load_config

config = load_config()
logger = get_logger(__name__, level=config.log_level, log_to_file=config.log_to_file, log_file_path=config.log_file_path)

def load_ids_from_file(file_path: str) -> List[str]:
    ext = os.path.splitext(file_path)[1]
    ids = []

    if ext == ".txt":
        with open(file_path, "r") as f:
            ids = [line.strip() for line in f if line.strip()]
    elif ext == ".csv":
        with open(file_path, "r") as f:
            reader = csv.DictReader(f)
            if 'pmc_id' not in reader.fieldnames:
                raise ValueError("CSV must contain a 'pmc_id' column")
            ids = [row['pmc_id'].strip() for row in reader]
    elif ext == ".json":
        with open(file_path, "r") as f:
            ids = json.load(f)
        if not isinstance(ids, list):
            raise ValueError("JSON file must contain a list of PMC IDs")
    else:
        raise ValueError(f"Unsupported file format: {ext}")
    
    logger.info(f"Loaded {len(ids)} IDs from {file_path}")
    return ids

def run_batch_ingest(file_path: str):
    try:
        pmc_ids = load_ids_from_file(file_path)
        papers = ingest_pmc_ids(pmc_ids)

        writer = DuckDBWriter()
        for paper in papers:
            writer.insert_paper(paper)

        logger.info(f"Batch ingestion completed successfully for file: {file_path}")
        raise typer.Exit(code=0)

    except typer.Exit:
        raise

    except Exception as e:
        logger.error(f"Batch ingestion failed: {e}")
        raise typer.Exit(code=1)