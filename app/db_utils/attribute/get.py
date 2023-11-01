import app.db.connection as conn
from decouple import config
from app.schema.atribute.get import GetAttributeAll, GetPersonsPhoto
from uuid import UUID
from app.schema.atribute.utils.base import TypeEnum
from app.schema.atribute.utils.base import Point


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


async def get_person_by_photo(photo_id: UUID) -> list[GetPersonsPhoto]:
    query = f"""SELECT id, first_point, second_point, confidence FROM {config('ATTRIBUTE_TABLE')} 
    WHERE photo_id = $1 AND type = $2 """

    connection = await conn.connection()
    records = await connection.fetch(query, photo_id, TypeEnum.person)
    record_list = []
    for record in records:
        model = GetPersonsPhoto(id=record.get('id'),
                                first_point=Point(x_position=record.get('first_point').x,
                                                  y_position=record.get('first_point').y),
                                second_point=Point(x_position=record.get('second_point').x,
                                                   y_position=record.get('second_point').y),
                                confidence=record.get('confidence'))
        record_list.append(model)

    return record_list
