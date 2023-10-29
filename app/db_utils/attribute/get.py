import app.db.connection as conn
from decouple import config
from app.schema.atribute.get import GetAttributeAll


async def get_by_photo(photo_id) -> list[GetAttributeAll]:
    query = f"""SELECT photo_id, person_id, type, positionX, positionY FROM {config('ATTRIBUTE_TABLE')} 
    WHERE photo_id = $1 
    """

    connection = await conn.connection()
    records = await connection.fetch(query, photo_id)
    await conn.close_connection(connection)
    records_list = []
    for record in records:
        model = GetAttributeAll(**record)
        records_list.append(model)

    return records_list

