from pydantic import BaseModel


class GetAttributeAll(BaseModel):
    positionX: int
    positionY: int
    type: str
    photo_id: str
    person_id: str

