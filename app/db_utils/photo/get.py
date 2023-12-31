import app.db.connection as conn
from app.schema.photo.get import GetCountIntruder, GetPhoto
from decouple import config
from loguru import logger
from uuid import UUID
from typing import Optional


async def get_id(photo_id: UUID) -> GetPhoto:
    try:
        query = f"SELECT id, source, date, intruder FROM {config('PHOTO_TABLE')} WHERE id = $1"
        connection = await conn.connection()

        record = await connection.fetchrow(query, photo_id)
        record = GetPhoto(**record)
        return record
    except Exception as error:
        logger.error(error)


async def get_count_intruder(photo_id: UUID) -> Optional[GetCountIntruder]:
    query = f"""SELECT intruder FROM {config("PHOTO_TABLE")} WHERE id = $1"""

    connection = await conn.connection()

    record = await connection.fetchval(query, photo_id)
    await conn.close_connection(connection)
    if record is None:
        return None

    return GetCountIntruder(intruder_count=record)
