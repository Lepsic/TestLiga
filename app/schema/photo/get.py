from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime


class GetPhoto(BaseModel):
    id: UUID
    source: str
    date: datetime
    intruder: int = Field(default=-1)  # елси значение еще не определено
