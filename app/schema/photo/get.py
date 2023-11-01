from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime


class GetPhoto(BaseModel):
    id: UUID
    source: str
    date: datetime
    intruder: int = Field(default=None)  # елси значение еще не определено


class GetCountIntruder(BaseModel):
    intruder_count: int
