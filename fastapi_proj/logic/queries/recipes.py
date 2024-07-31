from dataclasses import dataclass

from fastapi_proj.infra.cache.basestorages import BaseCacheStorage
from fastapi_proj.infra.repositories.recipies.base import BaseRecipeRepository
from fastapi_proj.infra.repositories.users.base import BaseUserRepository
from fastapi_proj.logic.queries.base import BaseQuery, BaseQueryHandler


@dataclass(frozen=True)
class SearchQuery(BaseQuery):
    q: str


@dataclass
class SearchQueryHandler(BaseQueryHandler[SearchQuery, list[dict] | None]):
    recipe_repository: BaseRecipeRepository

    async def handle(self, query: SearchQuery) -> list[dict] | None:
        return await self.recipe_repository.search_for_recipe(query.q)


@dataclass(frozen=True)
class GetPopularRecipesQuery(BaseQuery):
    limit: int
    offset: int


@dataclass
class GetPopularRecipesHandler(BaseQueryHandler[GetPopularRecipesQuery, list]):
    recipe_repository: BaseRecipeRepository
    cache_storage: BaseCacheStorage

    async def handle(self, command: GetPopularRecipesQuery) -> list:
        cache_key = f"/recipes/popular?limit={command.limit}&offset={command.offset}"
        cached = await self.cache_storage.get_by_key(cache_key)
        if not cached:
            recipes = await self.recipe_repository.get_popular_recipes(
                command.limit, command.offset
            )
            await self.cache_storage.set_key(cache_key, recipes, 120)
            return recipes
        return cached


@dataclass(frozen=True)
class GetRecipeByIdQuery(BaseQuery):
    username: str
    recipe_id: str


@dataclass
class GetRecipeByIdHandler(BaseQueryHandler[GetRecipeByIdQuery, dict | None]):
    user_repository: BaseUserRepository
    recipe_repository: BaseRecipeRepository

    async def handle(self, command: GetRecipeByIdQuery) -> dict | None:
        is_liked = await self.user_repository.check_is_recipe_liked(
            command.username, command.recipe_id
        )
        result = await self.recipe_repository.get_by_id(command.recipe_id)
        if result:
            result["is_liked"] = is_liked
        return result
