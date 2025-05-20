from dataclasses import field
from typing import List, Optional, Dict
from pydantic import BaseModel

class FigureData(BaseModel):
    figure_name: str
    figure_caption: str 
    # entities: List[Dict[str, str]]
    # entities: List[Entity]
    entities: Optional[List[Dict[str, str]]] = field(default_factory=list)