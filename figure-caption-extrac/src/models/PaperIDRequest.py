from pydantic import BaseModel

class PaperIDRequest(BaseModel):
    ids: list[str]