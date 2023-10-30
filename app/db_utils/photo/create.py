import app.db.connection as conn
from app.schema.photo.create import CreatePhoto
from decouple import config
from loguru import logger


async def create(model: CreatePhoto) -> None:
    try:
        query = f"""INSERT INTO {config('PHOTO_TABLE')} (source) VALUES($1)"""
        connection = await conn.connection()
        await connection.execute(query, model.photo_source,)
    except Exception as error:
        logger.error(error)
