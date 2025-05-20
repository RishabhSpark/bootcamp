import duckdb
import os
import json
from src.models.PaperData import PaperData
from src.utils.logger import get_logger
from src.config.config_loader import load_config

config = load_config()
logger = get_logger(__name__, level=config.log_level, log_to_file=config.log_to_file, log_file_path=config.log_file_path)

class DuckDBWriter:
    def __init__(self, db_path: str = config.db_path):
        self.db_path = db_path
        db_dir = os.path.dirname(db_path)
        # Ensure the directory exists
        if not os.path.exists(db_dir):
            try:
                os.makedirs(db_dir, exist_ok=True)
                logger.info(f"Created directory for DuckDB at: {db_dir}")
            except Exception as e:
                logger.error(f"Failed to create directory {db_dir}: {e}")
                raise
        else:
            logger.debug(f"Directory already exists for DuckDB: {db_dir}")
        
        self.conn = duckdb.connect(database=db_path)
        logger.info(f"DuckDB connected at: {db_path}")
        self._initialize_tables()

    def _initialize_tables(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS papers (
                pmcid TEXT,
                title TEXT,
                abstract TEXT
            )
        """)
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS figures (
                pmcid TEXT,
                figure_name TEXT,
                figure_caption TEXT,
                entities TEXT
            )
        """)
        logger.debug("DuckDB tables ensured.")

    def insert_paper(self, paper: PaperData):
        # Check if paper already exists
        exists = self.conn.execute(
            "SELECT 1 FROM papers WHERE pmcid = ? LIMIT 1", (paper.pmcid,)
        ).fetchone()

        if exists:
            logger.info(f"Paper {paper.pmcid} already exists, skipping insertion.")
            return

        # Insert paper
        self.conn.execute(
            "INSERT INTO papers (pmcid, title, abstract) VALUES (?, ?, ?)",
            (paper.pmcid, paper.title, paper.abstract)
        )

        # Insert figures, avoid duplicates by figure_name
        for fig in paper.figures:
            fig_exists = self.conn.execute(
                "SELECT 1 FROM figures WHERE pmcid = ? AND figure_name = ? LIMIT 1",
                (paper.pmcid, fig.figure_name)
            ).fetchone()

            if not fig_exists:
                self.conn.execute(
                    "INSERT INTO figures (pmcid, figure_name, figure_caption, entities) VALUES (?, ?, ?, ?)",
                    (paper.pmcid, fig.figure_name, fig.figure_caption, json.dumps(fig.entities))
                )
        logger.info(f"Inserted paper {paper.pmcid} with {len(paper.figures)} figures.")
        
    
    def export_to_csv(self, output_dir: str):
        os.makedirs(output_dir, exist_ok=True)
        logger.info(f"Exporting to CSV in {output_dir}")

        papers_df = self.conn.execute("SELECT * FROM papers").fetchdf()
        figures_df = self.conn.execute("SELECT * FROM figures").fetchdf()

        papers_df.to_csv(os.path.join(output_dir, "papers.csv"), index=False)
        figures_df.to_csv(os.path.join(output_dir, "figures.csv"), index=False)
        logger.info("CSV export completed.")

    def export_to_json(self, output_dir: str):
        os.makedirs(output_dir, exist_ok=True)
        logger.info(f"Exporting to JSON in {output_dir}")

        papers_df = self.conn.execute("SELECT * FROM papers").fetchdf()
        figures_df = self.conn.execute("SELECT * FROM figures").fetchdf()
        figures_df['entities'] = figures_df['entities'].apply(lambda x: json.loads(x) if isinstance(x, str) else x)
        
        papers_df.to_json(os.path.join(output_dir, "papers.json"), orient="records", indent=2)
        figures_df.to_json(os.path.join(output_dir, "figures.json"), orient="records", indent=2)
        
        logger.info("JSON export completed.")