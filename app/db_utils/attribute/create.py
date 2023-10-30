import app.db.connection as conn
from loguru import logger
from decouple import config
from app.schema.atribute import CreateAttribute, CreatePerson


async def create_attribute(model: CreateAttribute) -> None:
    try:
        query = f"""
        
        INSERT INTO {config('ATTRIBUTE_TABLE')} (person_id, photo_id, type, positionX, positionY, confidence)
        VALUES($1, $2, $3, $4, $5, $6)
        
        """

        connection = await conn.connection()
        await connection.execute(query, model.person_id, model.photo_id, model.type, model.positionX, model.positionY,
                                 model.confidence)
    except Exception as error:
        logger.error(error)


async def create_person(model: CreatePerson) -> None:
    try:
        query = f"""INSERT INTO {config('ATTRIBUTE_TABLE')} (COALESCE(:person_id, :id), photo_id, type, positionX, 
        positionY, confidence)
            VALUES($1, $2, $3, $4, $5)"""

        connection = await conn.connection()
        await connection.execute(query, model.photo_id, model.type, model.positionX, model.positionY, model.confidence)
    except Exception as error:
        logger.error(error)
