from pydantic import BaseModel
from typing import Literal

class AppConfig(BaseModel):
    storage_backend: Literal["duckdb"]
    db_path: str
    api_key: str
    data_source: Literal["pmc"]
    log_level: Literal["debug", "info", "warning", "error"]
    log_to_file: bool
    log_file_path: str