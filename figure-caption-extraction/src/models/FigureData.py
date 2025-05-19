from typing import List, Dict
from pydantic import BaseModel

# class EntityData(BaseModel):
#     type: Optional[str]
#     text: Optional[str]
#     id: Optional[str]

class FigureData(BaseModel):
    figure_name: str
    figure_caption: str
    entities: List[Dict[str, str]]