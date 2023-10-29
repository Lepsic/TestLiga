from pydantic import BaseModel, Field
from uuid import UUID
from enum import Enum


class TypeEnum(str, Enum):
    helmet = 'helmet'
    suit = 'suit'
    person = 'person'


class CreateAttribute(BaseModel):
    positionX: int
    positionY: int
    type: TypeEnum = Field(enum=TypeEnum)
    photo_id: UUID
    person_id: UUID
