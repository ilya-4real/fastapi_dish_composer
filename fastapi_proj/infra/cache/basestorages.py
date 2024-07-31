import json
from abc import ABC, abstractmethod
from dataclasses import dataclass
from logging import getLogger
from typing import Any

logger = getLogger(__name__)


@dataclass
class BaseCacheStorage(ABC):
    host: str
    port: int
    username: str | None = None
    password: str | None = None

    @abstractmethod
    async def set_key(self, key: str, value: Any, ttl: int) -> None: ...

    @abstractmethod
    async def get_by_key(self, key: str) -> Any: ...

    @abstractmethod
    async def delete_key(self, key: str) -> None: ...

    @staticmethod
    def convert_value_to_json(data: Any) -> str:
        try:
            return json.dumps(data)
        except TypeError:
            logger.error(f"unable to json encode: {data}")
            return ""

    @staticmethod
    def convert_json_to_dict(data: str):
        try:
            return json.loads(data)
        except TypeError:
            logger.error(f"unable to decode object: {data}")
            return ""
