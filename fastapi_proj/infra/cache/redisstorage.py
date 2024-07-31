from dataclasses import dataclass, field
from typing import Any

import redis.asyncio as redis

from fastapi_proj.infra.cache.basestorages import BaseCacheStorage


@dataclass
class RedisCacheStorage(BaseCacheStorage):
    redis_client: redis.Redis = field(init=False)

    def __post_init__(self):
        self.redis_client = redis.Redis(host=self.host, port=self.port)

    async def set_key(self, key: str, value: Any, ttl: int) -> None:
        encoded_value = self.convert_value_to_json(value)
        await self.redis_client.set(key, encoded_value, ttl)

    async def get_by_key(self, key: str) -> Any:
        cached = await self.redis_client.get(key)
        return self.convert_json_to_dict(cached) or ""

    async def delete_key(self, key: str) -> None:
        await self.redis_client.delete(key)
