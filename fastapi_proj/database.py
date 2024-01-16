from beanie import Document 

from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @abstractmethod
    async def add_one():
        raise NotImplementedError
    
    async def get_one():
        raise NotImplementedError
    
    async def get_all():
        raise NotImplementedError
    

class BeanieRepository():
    model: Document = None