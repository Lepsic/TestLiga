from abc import ABC, abstractmethod


class ServiceBase(ABC):

    def __init__(self):
        self._error = None
        self._result = None

    @property
    def result(self):
        return self._result

    @property
    def error(self):
        return self._error

    @abstractmethod
    async def execute(self, *args, **kwargs):
        pass
