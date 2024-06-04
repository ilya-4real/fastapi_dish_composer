import logging
from functools import lru_cache

from motor.motor_asyncio import AsyncIOMotorClient
from punq import Container, Scope

from fastapi_proj.config import settings
from fastapi_proj.infra.repositories.recipies.base import (
    BaseComponentRepository,
    BaseRecipeRepository,
)
from fastapi_proj.infra.repositories.recipies.mongo import (
    MongoComponentRepository,
    MongoRecipeRepository,
)
from fastapi_proj.logic.comands.components import (
    CreateComponentCommand,
    CreateComponentCommandHandler,
    DeleteComponentByTitleCommand,
    DeleteComponentByTitleHandler,
    GetComponentByTitleCommand,
    GetComponentByTitleHandler,
    GetComponentsByCategory,
    GetComponentsByCategoryHandler,
    GetRandomComponentInCategoryCommand,
    GetRandomComponentInCategoryHandler,
    UpdateComponentByTitleCommand,
    UpdateComponentByTitleHandler,
)
from fastapi_proj.logic.mediator import Mediator

logger = logging.getLogger(__name__)


@lru_cache(1)
def init_container() -> Container:
    return _init_container()


def _init_container() -> Container:
    container = Container()

    mongo_client = AsyncIOMotorClient(settings.mongo_uri, serverSelectionTimeoutMS=3000)
    logger.debug(settings.mongo_uri)

    def init_mongo_component_rep():
        return MongoComponentRepository(
            mongo_client,
            settings.mongo_db_name,
            settings.mongo_component_collection,
        )

    def init_mongo_recipe_rep():
        return MongoRecipeRepository(
            mongo_client,
            settings.mongo_db_name,
            settings.mongo_recipe_collection,
        )

    container.register(
        BaseComponentRepository,
        factory=init_mongo_component_rep,
        scope=Scope.singleton,
    )

    container.register(
        BaseRecipeRepository,
        factory=init_mongo_recipe_rep,
        scope=Scope.singleton,
    )

    def init_mediator():
        mediator = Mediator()
        mediator.register_command(
            CreateComponentCommand,
            [
                CreateComponentCommandHandler(
                    container.resolve(BaseComponentRepository)  # type: ignore
                )
            ],
        )

        mediator.register_command(
            GetComponentsByCategory,
            [
                GetComponentsByCategoryHandler(
                    container.resolve(BaseComponentRepository)  # type: ignore
                )
            ],
        )

        mediator.register_command(
            GetComponentByTitleCommand,
            [
                GetComponentByTitleHandler(
                    container.resolve(BaseComponentRepository)  # type: ignore
                )
            ],
        )
        mediator.register_command(
            GetRandomComponentInCategoryCommand,
            [
                GetRandomComponentInCategoryHandler(
                    container.resolve(BaseComponentRepository)  # type: ignore
                )
            ],
        )
        mediator.register_command(
            DeleteComponentByTitleCommand,
            [
                DeleteComponentByTitleHandler(
                    container.resolve(BaseComponentRepository)  # type: ignore
                )
            ],
        )

        mediator.register_command(
            UpdateComponentByTitleCommand,
            [
                UpdateComponentByTitleHandler(
                    container.resolve(BaseComponentRepository)  # type: ignore
                )
            ],
        )
        return mediator

    container.register(Mediator, factory=init_mediator, scope=Scope.singleton)

    return container
