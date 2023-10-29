from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class GetPhoto(BaseModel):
    id: UUID
    source: str
    date: datetime
    intruder: int

