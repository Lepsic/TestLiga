from app.schema.atribute.save import AttributeSave
from app.schema.atribute.create import CreateAttributesPerson, TypeEnum, Attribute, CreateAttributes
from app.service.base import ServiceBase
from app.db_utils.attribute.create import create_attribute
from fastapi import HTTPException, status
from loguru import logger
from typing import List


class SavePersonService(ServiceBase):
    def __init__(self):
        super().__init__()
        self.type = TypeEnum.person
        self.photo_id = None
        self._result = None

    async def execute(self, persons_model: CreateAttributesPerson):
        self.photo_id = persons_model.photo_id
        try:
            await self._save(self._get_attributes(persons_model.attribute))
        except Exception as error:
            self._error = error
            logger.error(error)
            return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=self._error)

    async def _save(self, models: List[AttributeSave]) -> None:
        for model in models:
            try:
                await create_attribute(model)
            except Exception as error:
                logger.error(error)
                self._error = error

    def _get_attributes(self, models: List[Attribute]) -> List[AttributeSave]:
        attribute_list = []
        for model in models:
            attribute_save = AttributeSave(photo_id=self.photo_id, type=self.type, **dict(model))
            attribute_list.append(attribute_save)
        return attribute_list


class SaveAttributes(ServiceBase):

    def __init__(self):
        super().__init__()
        self._type = None
        self._photo_id = None
        self._result = None

    async def execute(self, attributes_model: CreateAttributes):
        self._type = attributes_model.type
        self._photo_id = attributes_model.photo_id
        try:
            await self._save(self._get_attributes(attributes_model.attribute))
        except Exception as error:
            logger.error(error)
            self._error = error

    async def _save(self, models: List[AttributeSave]) -> None:
        for model in models:
            try:
                await create_attribute(model)
            except Exception as error:
                logger.error(error)
                self._error = error

    def _get_attributes(self, models: List[Attribute]) -> List[AttributeSave]:
        attribute_list = []
        for model in models:
            attribute_save = AttributeSave(photo_id=self._photo_id, type=self._type, **dict(model))
            attribute_list.append(attribute_save)
        return attribute_list
