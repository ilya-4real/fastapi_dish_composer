from abc import ABC, abstractmethod

class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError
    
    async def get_one():
        raise NotImplementedError
    
    async def get_all():
        raise NotImplementedError
    

class BeanieRepository(AbstractRepository):
    model = None

    async def get_one():
        ...