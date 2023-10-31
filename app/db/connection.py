from app.db.conf import *
import asyncpg
from loguru import logger


async def connection():
    try:
        connection = await asyncpg.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            host=DB_HOST,
            port=DB_PORT
        )
        return connection
    except Exception as error:
        logger.error(error)


async def close_connection(connect):
    await connect.close()


