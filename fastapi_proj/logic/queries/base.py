from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class BaseQuery(ABC): ...


@dataclass
class BaseQueryHandler[QT, QR](ABC):
    @abstractmethod
    async def handle(self, query: QT) -> QR:
        raise NotImplementedError
