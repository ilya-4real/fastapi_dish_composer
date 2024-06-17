import re
from abc import ABC
from dataclasses import dataclass
from logging import getLogger
from typing import Any

from motor.core import AgnosticClient
from pymongo.errors import DuplicateKeyError

from fastapi_proj.domain.enteties.component import Component, ComponentCategory
from fastapi_proj.domain.enteties.recipe import Recipe
from fastapi_proj.domain.exceptions.ingredients import (
    DuplicateComponentException,
)
from fastapi_proj.domain.values.components import CommonTitle
from fastapi_proj.infra.repositories.converters.converters import (
    convert_component_from_entity_to_document,
    convert_recipe_to_document,
)
from fastapi_proj.infra.repositories.recipies.base import (
    BaseComponentRepository,
    BaseRecipeRepository,
)

logger = getLogger(__name__)


@dataclass
class AbstractMongoRepository(ABC):
    mongo_client: AgnosticClient
    mongo_db_name: str
    mongo_collection: str

    @property
    def _collection(self):
        return self.mongo_client[self.mongo_db_name][self.mongo_collection]


@dataclass
class MongoComponentRepository(BaseComponentRepository, AbstractMongoRepository):
    async def add_component(self, component: Component) -> None:
        try:
            await self._collection.insert_one(
                convert_component_from_entity_to_document(component)
            )
        except DuplicateKeyError:
            raise DuplicateComponentException(402)

    async def get_components_by_category(
        self, category: str, limit: int, offset: int
    ) -> list[dict]:
        cursor = (
            self._collection.find(filter={"category": category})
            .limit(limit)
            .skip(offset)
        )
        result = await cursor.to_list(limit)
        logger.debug(result)
        return result

    async def get_random_component_by_category(
        self, category: ComponentCategory
    ) -> dict[str, Any]:  # type: ignore
        cursor = self._collection.aggregate(
            [
                {"$match": {"category": category.value}},
                {"$sample": {"size": 1}},
            ]
        )
        return await cursor.next()

    async def get_component_by_title(self, title: CommonTitle) -> dict:
        result = await self._collection.find_one(filter={"title": title.as_generic()})
        logger.debug(result)
        return result  # type: ignore

    async def delete_by_title(self, title: CommonTitle) -> None:
        await self._collection.delete_one(filter={"title": title.as_generic()})

    async def update_one_component_ingredients(self, component: Component) -> None:
        ingredients = [
            {"title": i.title.as_generic(), "amount": i.amount.as_generic()}
            for i in component.ingredients
        ]
        logger.debug(ingredients)
        await self._collection.update_one(
            {"title": component.title.as_generic()},
            {
                "$set": {
                    "ingredients": ingredients,
                }
            },
        )


@dataclass
class MongoRecipeRepository(BaseRecipeRepository, AbstractMongoRepository):
    async def add_recipe(self, recipe: Recipe) -> None:
        document = convert_recipe_to_document(recipe)
        await self._collection.insert_one(document)

    async def get_by_id(self, recipe_id: str) -> dict | None:
        result = await self._collection.find_one({"oid": recipe_id})
        logger.debug(result)
        return result

    async def increase_likes(self, recipe_id: str) -> None:
        await self._collection.update_one({"oid": recipe_id}, {"$inc": {"likes": 1}})

    async def decrease_likes(self, recipe_id: str) -> None:
        await self._collection.update_one({"oid": recipe_id}, {"$inc": {"likes": -1}})

    async def get_popular_recipes(self, limit: int, offset: int) -> list:
        cursor = (
            self._collection.find(
                {"likes": {"$gt": 0}},
                {
                    "_id": 0,
                    "oid": 1,
                    "title": 1,
                    "description": 1,
                    "author": 1,
                    "likes": 1,
                },
            )
            .sort("likes", -1)
            .skip(offset)
            .limit(limit)
        )
        result = [item async for item in cursor]
        logger.debug(result)
        return result

    async def search_for_recipe(self, q: str) -> list[dict] | None:
        regex = re.compile(f"^{q}", re.IGNORECASE)
        cursor = self._collection.find(
            {"title": regex}, {"_id": 0, "oid": 1, "title": 1}
        )
        return [i async for i in cursor]
