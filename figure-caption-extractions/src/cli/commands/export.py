import typer
from pathlib import Path
from src.storage.duckdb_writer import DuckDBWriter
from src.utils.logger import get_logger
from src.config.config_loader import load_config

export_app = typer.Typer(help="Export data from DuckDB")

config = load_config()
logger = get_logger(__name__, level=config.log_level, log_to_file=config.log_to_file, log_file_path=config.log_file_path)

@export_app.command("csv")
def to_csv(output_dir: Path = typer.Option(..., help="Directory to save CSV files")):
    """
    Export papers and figures to CSV files in the specified directory.
    """
    try:
        db_writer = DuckDBWriter()
        db_writer.export_to_csv(str(output_dir))
        logger.info(f"CSV export completed to folder: {output_dir}")
    except Exception as e:
        logger.error(f"CSV export failed: {e}")
        raise typer.Exit(code=1)


@export_app.command("json")
def to_json(output_dir: Path = typer.Option(..., help="Directory to save JSON files")):
    """
    Export papers and figures to JSON files in the specified directory.
    """
    try:
        db_writer = DuckDBWriter()
        db_writer.export_to_json(str(output_dir))
        logger.info(f"JSON export completed to folder: {output_dir}")
    except Exception as e:
        logger.error(f"JSON export failed: {e}")
        raise typer.Exit(code=1)