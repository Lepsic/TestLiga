from fastapi import APIRouter
from app.db_utils.attribute.create import create_attribute, create_persons
from app.db_utils.attribute.get import get_by_photo
from app.schema.atribute.create import CreateAttributesPerson, CreateAttributes
from loguru import logger
from app.service.save_attribute.save import SavePersonService, SaveAttributes

router = APIRouter()


@router.post("/create/persons")
async def create_persons_api(persons: CreateAttributesPerson) -> None:
    service = SavePersonService()
    await service.execute(persons)
    if bool(service.error):
        raise service.result
    else:
        return service.result


@router.post("/create/attributes")
async def create_attribute_api(attributes: CreateAttributes):
    service = SaveAttributes()
    await service.execute(attributes)
    if bool(service.error):
        raise service.result
    else:
        return service.result


router.add_api_route("/create/persons", create_persons_api, methods=["POST"])
router.add_api_route("/create/attributes", create_attribute_api, methods=["POST"])
