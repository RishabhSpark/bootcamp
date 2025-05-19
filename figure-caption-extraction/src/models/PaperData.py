from pydantic import BaseModel
from typing import List, Dict, Any
from src.models.FigureData import FigureData

class PaperData(BaseModel):
    pmcid: str
    title: str
    abstract: str
    figures: List[FigureData]
    