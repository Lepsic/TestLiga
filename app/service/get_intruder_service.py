from .base import ServiceBase
from uuid import UUID
from app.schema.photo.get import GetCountIntruder
from app.db_utils.photo.get import get_count_intruder
from loguru import logger
from app.db_utils.photo.save import save_count_intruder


class CountIntruderService(ServiceBase):
    def __init__(self, photo_id: UUID):
        super().__init__()
        self._photo_id = photo_id
        self._result = None

    async def execute(self) -> GetCountIntruder:
        try:
            self._result = await self._get_intruder()
            if self._result is None:
                self._result = await self._count_intruder()
            return self._result
        except Exception as error:
            self._error = error
            logger.error(error)

    async def _count_intruder(self) -> GetCountIntruder:
        """Считает количество нарушителей"""
        intruder_count = await save_count_intruder(self._photo_id)
        return intruder_count

    async def _get_intruder(self) -> GetCountIntruder:
        """Получает с бд хранимые там данные"""
        intruder_count = await get_count_intruder(self._photo_id)
        return intruder_count
