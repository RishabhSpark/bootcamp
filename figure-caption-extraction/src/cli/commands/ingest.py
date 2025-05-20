import typer
from pathlib import Path
from typing import List
from src.cli.batch_ingest import run_batch_ingest
from src.ingestion.ingest_pipeline import ingest_pmc_ids
from src.storage.duckdb_writer import DuckDBWriter
from src.utils.logger import get_logger
from src.config.config_loader import load_config

ingest_app = typer.Typer(help="Ingest PMC/PMID papers")

config = load_config()
logger = get_logger(__name__, level=config.log_level, log_to_file=config.log_to_file, log_file_path=config.log_file_path)

@ingest_app.command("file")
def from_file(file_path: Path):
    """
    Ingest paper IDs from a file (txt/csv/json).
    """
    logger.info(f"Reading IDs from file: {file_path}")
    if not file_path.exists():
        logger.error(f"File not found: {file_path}")
        raise typer.Exit(code=1)
    run_batch_ingest(str(file_path))

@ingest_app.command("list")
def from_list(ids: List[str]):
    """_
    Ingest paper IDs from a list via terminal.
    """
    logger.info(f"Recieved {len(ids)} to ingest.")
    
    duckdb_writer = DuckDBWriter()

    try:
        papers = ingest_pmc_ids(ids)
        for paper in papers:
            duckdb_writer.insert_paper(paper)
        logger.info(f"Successfully ingested {len(papers)} papers from CLI list.")
    except Exception as e:
        logger.error(f"Ingestion failed: {e}")
        raise typer.Exit(code=1)
    
@ingest_app.command("folder")
def from_folder(folder_path: Path):
    """
    Ingest paper IDs from all supported files in a folder.
    Supports: .txt, .csv, .json
    """
    logger.info(f"Reading IDs from folder: {folder_path}")
    if not folder_path.exists() or not folder_path.is_dir():
        logger.error(f"Folder not found or not a directory: {folder_path}")
        raise typer.Exit(code=1)
    
    from src.cli.batch_ingest import run_batch_ingest_folder
    
    run_batch_ingest_folder(str(folder_path))