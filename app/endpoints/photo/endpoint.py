from fastapi import APIRouter
from app.schema.photo.create import CreatePhoto
from app.schema.photo.get import GetPhoto, GetCountIntruder
from app.db_utils.photo.create import create
from app.db_utils.photo.get import get_id
from uuid import UUID
from app.service.get_intruder_service import CountIntruderService

router = APIRouter()


@router.post("/create/")
async def create_photo_api(photo: CreatePhoto):
    await create(photo)
    return {'result': 'success'}


@router.get("/get/{photo_id}")
async def get_photo(photo_id: UUID) -> GetPhoto:
    model = await get_id(photo_id)
    return model


@router.get("/get/intruder/{photo_id}")
async def get_intruder(photo_id: UUID) -> GetCountIntruder:
    service = CountIntruderService(photo_id)
    intruders = await service.execute()
    return intruders


router.add_api_route("/create/", create_photo_api, methods=["POST"])
router.add_api_route("/get/{photo_id}", get_photo, methods=["GET"])
router.add_api_route("/get/intruder/{photo_id}", get_intruder)
