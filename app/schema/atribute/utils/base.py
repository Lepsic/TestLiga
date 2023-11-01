from pydantic import BaseModel, Field
from uuid import UUID
from enum import Enum


class Point(BaseModel):
    """Представление точки"""
    x_position: float
    y_position: float




class TypeEnum(str, Enum):
    """Список доступных атрибутов"""
    helmet = 'helmet'
    suit = 'suit'
    person = 'person'


class Attribute(BaseModel):
    """Базовое представление атрибута"""
    first_point: Point
    second_point: Point
    confidence: float



