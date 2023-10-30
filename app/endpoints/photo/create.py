from fastapi import APIRouter
from app.schema.photo.create import CreatePhoto
from app.db_utils.photo.create import create

router = APIRouter()


@router.post("/create/")
async def create_photo(photo: CreatePhoto):
    await create(photo)
    return {'result': 'success'}


router.add_api_route("/create/", create_photo, methods=["POST"])
