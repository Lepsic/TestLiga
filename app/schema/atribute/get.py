from pydantic import BaseModel
from uuid import UUID
from app.schema.atribute.utils.base import Point

"""Получение втрибутов из бд"""


class GetAttributeAll(BaseModel):
    """Получение из бд целиком записи (Врятли нужно будет) """
    first_point: Point
    second_point: Point
    type: str
    photo_id: str
    person_id: str


class GetPersonsPhoto(BaseModel):
    """Получение person из бд """
    id: UUID
    first_point: Point
    second_point: Point
    confidence: float

