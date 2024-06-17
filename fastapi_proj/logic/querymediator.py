from collections import defaultdict
from dataclasses import dataclass, field

from fastapi_proj.logic.queries.base import BaseQuery, BaseQueryHandler


@dataclass
class QueryMediator:
    query_map: dict[type[BaseQuery], BaseQueryHandler] = field(
        default_factory=lambda: defaultdict()
    )

    def register_handler(self, query: type[BaseQuery], handler: BaseQueryHandler):
        self.query_map[query] = handler

    async def handle_query(self, query: BaseQuery):
        return await self.query_map[type(query)].handle(query)
