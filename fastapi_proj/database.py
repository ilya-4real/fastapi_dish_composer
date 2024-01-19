from beanie import Document

from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError

    @abstractmethod
    async def get_one():
        raise NotImplementedError

    @abstractmethod
    async def get_all():
        raise NotImplementedError


class BeanieRepository(AbstractRepository):
    model = None

    async def get_all(self):
        pass

    async def add_one(self):
        pass

    async def get_one(self):
        pass
