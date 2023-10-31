from enum import Enum
from uuid import UUID
from .create import Point
from pydantic import BaseModel, Field


class TypeEnum(str, Enum):
    helmet = 'helmet'
    suit = 'suit'
    person = 'person'


class AttributeSave(BaseModel):
    photo_id: UUID
    person_id: UUID = Field(default=None)
    type: TypeEnum
    first_point: Point
    second_point: Point
    confidence: float
