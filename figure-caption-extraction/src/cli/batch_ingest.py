import os
import csv
import json
from pathlib import Path
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
    
    
def collect_pmc_ids(path: str) -> List[str]:
    collected_ids = []
    path_obj = Path(path)

    if path_obj.is_file():
        collected_ids.extend(load_ids_from_file(str(path_obj)))

    elif path_obj.is_dir():
        supported_exts = {".txt", ".csv", ".json"}
        files = [f for f in path_obj.iterdir() if f.suffix in supported_exts and f.is_file()]

        if not files:
            logger.warning(f"No supported files (.txt, .csv, .json) found in folder: {path}")
        
        for file in files:
            try:
                ids = load_ids_from_file(str(file))
                collected_ids.extend(ids)
            except Exception as e:
                logger.error(f"Failed to load from {file.name}: {e}")
    
    else:
        raise ValueError(f"Provided path is neither a file nor a folder: {path}")

    logger.info(f"Total PMC IDs collected: {len(collected_ids)}")
    return collected_ids


def run_batch_ingest_folder(path: str):
    try:
        pmc_ids = collect_pmc_ids(path)
        papers = ingest_pmc_ids(pmc_ids)

        writer = DuckDBWriter()
        for paper in papers:
            writer.insert_paper(paper)

        logger.info(f"Batch ingestion completed successfully from: {path}")
        raise typer.Exit(code=0)

    except typer.Exit:
        raise

    except Exception as e:
        logger.error(f"Batch ingestion failed: {e}")
        raise typer.Exit(code=1)