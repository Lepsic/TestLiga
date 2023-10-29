from pydantic import BaseModel


class CreatePhoto(BaseModel):
    photo_source: str


