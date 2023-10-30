from fastapi import APIRouter
from app.schema.photo.create import CreatePhoto
from app.schema.photo.get import GetPhoto
from app.db_utils.photo.create import create
from app.db_utils.photo.get import get_id
from uuid import UUID

router = APIRouter()


@router.post("/create/")
async def create_photo_api(photo: CreatePhoto):
    await create(photo)
    return {'result': 'success'}


@router.get("/get/{photo_id}")
async def get_photo(photo_id: UUID) -> GetPhoto:
    model = await get_id(photo_id)
    return model


router.add_api_route("/create/", create_photo_api, methods=["POST"])
router.add_api_route("/get/{photo_id}", get_photo, methods=["GET"])
