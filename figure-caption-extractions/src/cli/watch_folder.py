import time
import shutil
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from src.ingestion.ingest_pipeline import ingest_pmc_ids
from src.storage.duckdb_writer import DuckDBWriter
from src.utils.logger import get_logger
from src.config.config_loader import load_config

config = load_config()
logger = get_logger(__name__, level=config.log_level, log_to_file=config.log_to_file, log_file_path=config.log_file_path)

class PaperIDFileHandler(FileSystemEventHandler):
    def __init__(self, duckdb_writer: DuckDBWriter, base_dir: Path):
        self.duckdb_writer = duckdb_writer
        self.unprocessed_dir = base_dir / "unprocessed"
        self.underprocess_dir = base_dir / "underprocess"
        self.processed_dir = base_dir / "processed"
        self.failed_dir = base_dir / "failed"

        # Ensure all required folders exist
        for d in [self.unprocessed_dir, self.underprocess_dir, self.processed_dir, self.failed_dir]:
            d.mkdir(parents=True, exist_ok=True)

    def on_created(self, event):
        print(f'on_created called with: {event.src_path}')
        if event.is_directory:
            return

        src_file = Path(event.src_path)

        if src_file.parent != self.unprocessed_dir:
            logger.debug(f"Ignoring file outside unprocessed/: {src_file}")
            return

        if src_file.suffix.lower() != ".txt":
            logger.info(f"Ignored non-txt file: {src_file.name}")
            return

        logger.info(f"Detected new unprocessed file: {src_file.name}")

        try:
            # Move to underprocess
            underprocess_file = self.underprocess_dir / src_file.name
            shutil.move(str(src_file), str(underprocess_file))
            logger.info(f"Moved file to underprocess/: {underprocess_file.name}")

            # Read and ingest
            ids = [line.strip() for line in underprocess_file.read_text().splitlines() if line.strip()]
            if not ids:
                logger.warning(f"No IDs found in {underprocess_file.name}, skipping.")
                shutil.move(str(underprocess_file), self.failed_dir / underprocess_file.name)
                return

            papers = ingest_pmc_ids(ids)
            for paper in papers:
                self.duckdb_writer.insert_paper(paper)
            logger.info(f"Ingested {len(papers)} papers from {underprocess_file.name}")

            # Move to processed
            shutil.move(str(underprocess_file), self.processed_dir / underprocess_file.name)
            logger.info(f"Moved to processed/: {underprocess_file.name}")

        except Exception as e:
            logger.error(f"Error processing {src_file.name}: {e}")
            try:
                shutil.move(str(underprocess_file), self.failed_dir / underprocess_file.name)
                logger.info(f"Moved failed file to failed/: {underprocess_file.name}")
            except Exception as move_err:
                logger.error(f"Failed to move to failed/: {move_err}")


def watch_folder(base_dir: Path):
    """
    Watches 'unprocessed/' subfolder inside base_dir for new files and processes them.
    """
    duckdb_writer = DuckDBWriter()
    handler = PaperIDFileHandler(duckdb_writer, base_dir)
    observer = Observer()
    observer.schedule(handler, str(handler.unprocessed_dir), recursive=False)
    observer.start()

    logger.info(f"Watching folder: {handler.unprocessed_dir}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("Stopping folder watcher due to keyboard interrupt.")
        observer.stop()

    observer.join()
    logger.info("Folder watcher stopped cleanly.")