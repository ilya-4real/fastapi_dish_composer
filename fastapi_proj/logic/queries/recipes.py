from dataclasses import dataclass

from fastapi_proj.infra.repositories.recipies.base import BaseRecipeRepository
from fastapi_proj.logic.queries.base import BaseQuery, BaseQueryHandler


@dataclass(frozen=True)
class SearchQuery(BaseQuery):
    q: str


@dataclass
class SearchQueryHandler(BaseQueryHandler[SearchQuery, list[dict] | None]):
    recipe_repository: BaseRecipeRepository

    async def handle(self, query: SearchQuery) -> list[dict] | None:
        return await self.recipe_repository.search_for_recipe(query.q)
