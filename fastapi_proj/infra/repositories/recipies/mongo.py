from abc import ABC
from dataclasses import dataclass

from motor.core import AgnosticClient

from fastapi_proj.domain.enteties.component import Component, ComponentCategory
from fastapi_proj.domain.enteties.recipe import Recipe
from fastapi_proj.infra.repositories.converters.converters import (
    convert_component_from_entity_to_document,
)
from fastapi_proj.infra.repositories.recipies.base import (
    BaseComponentRepository,
    BaseRecipeRepository,
)


@dataclass
class AbstractMongoRepository(ABC):
    mongo_client: AgnosticClient
    mongo_db_name: str
    mongo_collection: str

    @property
    def _collection(self):
        return self.mongo_client[self.mongo_db_name][self.mongo_collection]


@dataclass
class MongoComponentRepository(
    BaseComponentRepository, AbstractMongoRepository
):
    async def add_component(self, component: Component) -> None:
        await self._collection.insert_one(
            convert_component_from_entity_to_document(component)
        )

    async def get_random_component_by_category(
        self, category: ComponentCategory
    ) -> Component: ...


@dataclass
class MongoRecipeRepository(BaseRecipeRepository, AbstractMongoRepository):
    async def add_recipe(self, recipe: Recipe) -> None: ...
