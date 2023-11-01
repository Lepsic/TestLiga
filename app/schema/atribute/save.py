from enum import Enum
from uuid import UUID
from app.schema.atribute.utils.base import Point, Attribute
from pydantic import BaseModel, Field

"""Здесь происходит сохранение атрибутов в бд"""


class TypeEnum(str, Enum):
    helmet = 'helmet'
    suit = 'suit'
    person = 'person'


class AttributeSave(BaseModel):
    """Сохранение любого атрибута"""
    photo_id: UUID
    person_id: UUID = Field(default=None)
    type: TypeEnum
    first_point: Point
    second_point: Point
    confidence: float


class CreateAttributesBD(BaseModel):
    """Создание атрибутов уже непосредственно в бд"""
    photo_id: UUID
    person_id: UUID = Field(default=None)
    attribute: Attribute
