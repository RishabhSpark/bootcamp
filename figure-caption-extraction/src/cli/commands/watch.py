from pathlib import Path
import typer
from src.utils.logger import get_logger
from src.config.config_loader import load_config
from src.cli.watch_folder import watch_folder

watch_app = typer.Typer(help="Watch the folder")

config = load_config()
logger = get_logger(__name__, level=config.log_level, log_to_file=config.log_to_file, log_file_path=config.log_file_path)

@watch_app.command("watch")
def watch(
    base_dir: Path = typer.Option(..., exists=True, file_okay=False, dir_okay=True, writable=True,
                               help="Base folder path for the entire watch process folder")
):
    """
    Watch a folder continuously for new text files with paper IDs and ingest them.
    """
    logger.info(f"Starting to watch folder: {base_dir}/unprocessed/")
    watch_folder(base_dir)