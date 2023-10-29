import app.db.connection as conn
from loguru import logger
from decouple import config
from app.schema.atribute import CreateAttribute


async def create(model: CreateAttribute) -> None:
    try:
        query = f"""
        
        INSERT INTO {config('ATTRIBUTE_TABLE')} (person_id, photo_id, type, positionX, positionY), 
        VALUES($1, $2, $3, $4, $5)
        
        """
        connection = await conn.connection()
        await connection.execute(query, model.person_id, model.photo_id, model.type, model.positionX, model.positionY)
    except Exception as error:
        logger.error('Error created attribute', error)
