import app.db.connection as conn
from app.schema.photo.get import GetCountIntruder, GetPhoto
from app.schema.atribute.utils.base import TypeEnum
from decouple import config
from loguru import logger
from uuid import UUID


async def save_count_intruder(photo_id: UUID) -> GetCountIntruder:
    query = f"""
        UPDATE {config("PHOTO_TABLE")}
        SET intruder = (
            SELECT COUNT(*)
            FROM {config("ATTRIBUTE_TABLE")}
            WHERE type = $1 AND id NOT IN 
            (SELECT DISTINCT person_id FROM {config("ATTRIBUTE_TABLE")} WHERE person_id IS NOT NULL) AND photo_id = $2
        )
         RETURNING intruder """

    connection = await conn.connection()

    record = await connection.fetchval(query, TypeEnum.person, photo_id)
    await conn.close_connection(connection)

    return GetCountIntruder(intruder_count=record)
