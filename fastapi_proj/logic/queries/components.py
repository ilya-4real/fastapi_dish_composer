from dataclasses import dataclass
from typing import Any

from fastapi_proj.domain.enteties.component import ComponentCategory
from fastapi_proj.infra.repositories.recipies.base import BaseComponentRepository
from fastapi_proj.logic.queries.base import BaseQuery, BaseQueryHandler


@dataclass(frozen=True)
class QueryComponentById(BaseQuery):
    component_id: str


@dataclass
class QueryComponentHandler(BaseQueryHandler[QueryComponentById, dict]):
    component_repository: BaseComponentRepository

    async def handle(self, query: QueryComponentById) -> dict:
        return await self.component_repository.get_component_by_id(query.component_id)


@dataclass(frozen=True)
class GetRandomComponentInCategoryQuery(BaseQuery):
    category: ComponentCategory


@dataclass
class GetRandomComponentInCategoryHandler(
    BaseQueryHandler[GetRandomComponentInCategoryQuery, dict[str, Any]]
):
    component_repository: BaseComponentRepository

    async def handle(
        self, command: GetRandomComponentInCategoryQuery
    ) -> dict[str, Any]:
        return await self.component_repository.get_random_component_by_category(
            command.category
        )
