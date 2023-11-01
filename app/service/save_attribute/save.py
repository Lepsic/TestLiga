from app.schema.atribute.save import AttributeSave
from app.schema.atribute.create import CreateAttributesPersons, TypeEnum, Attribute, CreateAttributes
from app.service.base import ServiceBase
from app.db_utils.attribute.create import create_attribute
from fastapi import HTTPException, status
from loguru import logger
from typing import List
from app.db_utils.attribute.get import get_person_by_photo
from app.schema.atribute.get import GetPersonsPhoto


class SavePersonService(ServiceBase):
    def __init__(self):
        super().__init__()
        self.type = TypeEnum.person
        self.photo_id = None
        self._result = None

    async def execute(self, persons_model: CreateAttributesPersons):
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

    async def tests(self):
        return await get_person_by_photo(self._photo_id)

    async def execute(self, attributes_model: CreateAttributes):
        self._type = attributes_model.type
        self._photo_id = attributes_model.photo_id
        try:
            attributes = await self._related(await self._get_persons_photo(),
                                            await self._get_attributes(attributes_model.attribute))
            await self._save(attributes)
        except Exception as error:
            logger.error(error)
            self._error = error
            self._result = error

    async def _save(self, models: List[AttributeSave]) -> None:
        for model in models:
            try:
                await create_attribute(model)
            except Exception as error:
                logger.error(error)
                self._error = error

    async def _get_attributes(self, models: list[Attribute]) -> List[AttributeSave]:
        attribute_list = []
        for model in models:
            attribute_save = AttributeSave(photo_id=self._photo_id, type=self._type, **dict(model))
            attribute_list.append(attribute_save)
        return attribute_list

    async def _get_persons_photo(self) -> list[GetPersonsPhoto]:
        """Получение person из бд"""
        persons = await get_person_by_photo(self._photo_id)
        return persons

    async def _related(self, persons: list[GetPersonsPhoto], attributes: list[AttributeSave]) -> list[AttributeSave]:
        """Здесь идет привязка задается привязка к person переданных атрибутов"""
        used_id = []
        for attribute in attributes:
            for person in persons:
                if self._check(person, attribute):
                    attribute.person_id = person.id
                    if person.id in used_id:
                        person_save_instance = AttributeSave(photo_id=self._photo_id, type=TypeEnum.person,
                                                             **dict(person))
                        attribute.person_id = await create_attribute(person_save_instance, returned=True)
                    else:
                        used_id.append(person.id)
        return attributes

    def _check(self, person: GetPersonsPhoto, attribute: AttributeSave) -> bool:
        if (person.first_point.x_position < attribute.first_point.x_position and
                person.first_point.y_position < attribute.first_point.y_position):
            if (person.second_point.x_position > attribute.first_point.x_position and
                    person.second_point.y_position > attribute.second_point.y_position):
                return True
        else:
            return False
