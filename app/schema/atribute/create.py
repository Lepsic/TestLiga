from pydantic import BaseModel, Field
from uuid import UUID
from enum import Enum
from typing import List


class TypeEnum(str, Enum):
    helmet = 'helmet'
    suit = 'suit'
    person = 'person'


class Point(BaseModel):
    x_position: int
    y_position: int


class Attribute(BaseModel):
    first_point: Point
    second_point: Point
    confidence: float


class CreateAttributesPerson(BaseModel):
    photo_id: UUID
    attribute: List[Attribute]


class CreateAttributes(BaseModel):
    photo_id: UUID
    type: TypeEnum
    attribute: List[Attribute]
