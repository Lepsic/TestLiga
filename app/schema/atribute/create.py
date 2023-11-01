from pydantic import BaseModel, Field
from uuid import UUID
from typing import List
from app.schema.atribute.utils.base import Attribute, TypeEnum


class CreateAttributesPersons(BaseModel):
    """Данные которые приходят от сетки"""
    photo_id: UUID
    attribute: List[Attribute]


class CreateAttributes(BaseModel):
    """Получение атрибутов(не person) от сетки"""
    photo_id: UUID
    person_id: UUID = Field(default=None)
    type: TypeEnum
    attribute: List[Attribute]



