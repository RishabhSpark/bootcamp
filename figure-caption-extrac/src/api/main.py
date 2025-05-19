import csv
import json
import io
from fastapi import FastAPI, Depends, HTTPException, logger
from typing import Optional

from fastapi.responses import StreamingResponse
from src.ingestion.ingest_pipeline import ingest_pmc_ids
from src.api.auth import get_api_key
from src.storage.duckdb_writer import DuckDBWriter
from src.models.PaperIDRequest import PaperIDRequest

from src.utils.logger import get_logger
from src.config.config_loader import load_config

config = load_config()
logger = get_logger(__name__, level=config.log_level, log_to_file=config.log_to_file, log_file_path=config.log_file_path)

app = FastAPI(title="Paper Metadata API", version="1.0.0")
db = DuckDBWriter()

@app.get("/", tags=["Info"])
def root():
    logger.info("Root endpoint hit.")
    return {
        "message": "Welcome to the Paper Metadata API",
        "endpoints": {
            "GET /papers": "List all paper metadata",
            "GET /figures": "List all figure metadata",
            "POST /submit-ids": "Submit list of PMCIDs to ingest",
            "GET /export": "Export data in CSV or JSON format",
            "Docs": "/docs"
        }
    }

@app.get("/papers", dependencies=[Depends(get_api_key)])
def get_papers(pmcid: Optional[str] = None):
    logger.info(f"Fetching papers. PMCID: {pmcid}")
    query = "SELECT * FROM papers"
    if pmcid:
        query += " WHERE pmcid = ?"
        return db.conn.execute(query, (pmcid,)).fetchall()
    return db.conn.execute(query).fetchall()

@app.get("/figures", dependencies=[Depends(get_api_key)])
def get_figures(pmcid: Optional[str] = None):
    logger.info(f"Fetching figures. PMCID: {pmcid}")
    query = "SELECT * FROM figures"
    if pmcid:
        query += " WHERE pmcid = ?"
        return db.conn.execute(query, (pmcid,)).fetchall()
    return db.conn.execute(query).fetchall()

@app.get("/papers/{pmcid}", dependencies=[Depends(get_api_key)])
def get_paper_details(pmcid: str):
    logger.info(f"Fetching details for paper: {pmcid}")
    paper = db.conn.execute("SELECT * FROM papers WHERE pmcid = ?", (pmcid,)).fetchone()
    figures = db.conn.execute("SELECT * FROM figures WHERE pmcid = ?", (pmcid,)).fetchall()
    return {"paper": paper, "figures": figures}

@app.post("/submit-ids", tags=["Ingestion"])
def submit_ids(payload: PaperIDRequest, x_api_key: str = Depends(get_api_key)):
    logger.info(f"Received {len(payload.ids)} IDs for ingestion.")
    duckdb_writer = DuckDBWriter()
    try:
        papers = ingest_pmc_ids(payload.ids)
        for paper in papers:
            duckdb_writer.insert_paper(paper)
        logger.info(f"Successfully ingested {len(papers)} papers.")
        return {"message": f"Successfully ingested {len(papers)} papers."}
    except Exception as e:
        logger.error(f"Ingestion failed: {e}")
        raise HTTPException(status_code=500, detail="Ingestion failed.")
    
@app.get("/export", dependencies=[Depends(get_api_key)])
def export_data(table: str, format: str = "json"):
    logger.info(f"Exporting data from table '{table}' in format '{format}'")
    if table not in ("papers", "figures"):
        logger.warning(f"Invalid table name: {table}")
        raise HTTPException(status_code=400, detail="Invalid table name")
    
    query = f"SELECT * FROM {table}"
    rows = db.conn.execute(query).fetchall()
    columns = [desc[1] for desc in db.conn.execute(f"PRAGMA table_info('{table}')").fetchall()]
    
    if format == "json":
        # return rows
        data = [dict(zip(columns, row)) for row in rows]

        # Create JSON string
        json_str = json.dumps(data, indent=2)

        # Return StreamingResponse with attachment headers
        stream = io.StringIO(json_str)
        stream.seek(0)
        
        logger.info(f"Returning {len(data)} records as JSON")
        
        return StreamingResponse(
            stream,
            media_type="application/json",
            headers={"Content-Disposition": f"attachment; filename={table}.json"}
        )

    elif format == "csv":
        stream = io.StringIO()
        writer = csv.writer(stream)
        writer.writerow(columns)
        writer.writerows(rows)
        stream.seek(0)
        
        logger.info(f"Returning {len(rows)} records as CSV")

        return StreamingResponse(stream, media_type="text/csv",
                                 headers={"Content-Disposition": f"attachment; filename={table}.csv"})
    else:
        logger.warning(f"Invalid export format requested: {format}")
        raise HTTPException(status_code=400, detail="Invalid format. Use json or csv.")