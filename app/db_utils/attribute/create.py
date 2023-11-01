import app.db.connection as conn
from loguru import logger
from decouple import config
from uuid import UUID
from typing import Optional

from app.schema.atribute.create import CreateAttributesPersons
from app.schema.atribute.save import AttributeSave


async def create_attribute(model: AttributeSave, returned=False) -> Optional[UUID]:
    try:
        query_person = f"""
        
        INSERT INTO {config('ATTRIBUTE_TABLE')} (photo_id, confidence, type, first_point, second_point, person_id)
        VALUES($1, $2, $3, POINT($4, $5), POINT($6, $7), $8)
        
        """
        query_not_person = f"""
        
        INSERT INTO {config('ATTRIBUTE_TABLE')} (photo_id, confidence, type, first_point, second_point)
        VALUES($1, $2, $3, POINT($4, $5), POINT($6, $7))
        
        """
        query_last_object = f"""SELECT id FROM {config('ATTRIBUTE_TABLE')} ORDER BY id DESC LIMIT 1"""
        connection = await conn.connection()
        if model.person_id:
            await connection.execute(query_person, model.photo_id, model.confidence, model.type,
                                     model.first_point.x_position, model.first_point.y_position,
                                     model.second_point.x_position, model.second_point.y_position, model.person_id)
        else:
            await connection.execute(query_not_person, model.photo_id, model.confidence, model.type,
                                     model.first_point.x_position, model.first_point.y_position,
                                     model.second_point.x_position, model.second_point.y_position)
        if returned:
            pk = await connection.fetchrow(query_last_object)
            return pk['id']
    except Exception as error:
        logger.error(error)


async def create_persons(models: CreateAttributesPersons) -> None:
    try:
        query = f"""INSERT INTO {config('ATTRIBUTE_TABLE')} (COALESCE(:person_id, :id), photo_id, type, positionX, 
        positionY, confidence)
            VALUES($1, $2, $3, $4, $5)"""

        connection = await conn.connection()
        models_attribute = models.attribute
        for model in models_attribute:
            model.photo_id = models.photo_id
            await connection.execute(query, model.photo_id, model.type, model.positionX, model.positionY,
                                     model.confidence)
    except Exception as error:
        logger.error(error)
