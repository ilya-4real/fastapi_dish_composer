from dataclasses import dataclass
from logging import getLogger

from fastapi_proj.domain.enteties.recipe import Recipe
from fastapi_proj.domain.enteties.user import User
from fastapi_proj.infra.repositories.recipies.mongo import AbstractMongoRepository
from fastapi_proj.infra.repositories.users.base import BaseUserRepository

logger = getLogger(__name__)


@dataclass
class MongoUserRepository(AbstractMongoRepository, BaseUserRepository):
    async def get_or_create_new(self, username: str) -> User:
        user = await self._collection.find_one({"username": username})
        if not user:
            user = {
                "username": username,
                "liked_recipes": [],
                "created_recipes": [],
            }
            await self._collection.insert_one(user)
        del user["_id"]
        return User(**user)

    async def add_created_recipe(self, username: str, recipe_id: str) -> None:
        await self._collection.update_one(
            {"username": username},
            {"$push": {"created_recipes": {"recipe_id": recipe_id}}},
        )

    async def add_liked_recipe(self, username: str, recipe_id: str) -> None:
        await self._collection.update_one(
            {"username": username},
            {"$push": {"liked_recipes": {"recipe_id": recipe_id}}},
        )

    async def remove_liked_recipe(self, username: str, recipe_id: str) -> None:
        await self._collection.update_one(
            {"username": username},
            {"$pull": {"liked_recipes": {"recipe_id": recipe_id}}},
        )

    async def get_liked_recipes_by_username(self, username: str) -> dict:
        cursor = self._collection.aggregate(
            [
                {"$match": {"username": username}},
                {
                    "$lookup": {
                        "from": "recipies",
                        "localField": "liked_recipes.recipe_id",
                        "foreignField": "oid",
                        "as": "recipes",
                    }
                },
                {"$project": {"_id": 0, "recipes": 1}},
            ]
        )
        return await cursor.next()

    async def get_created_recipes_by_username(self, username: str) -> dict:
        cursor = self._collection.aggregate(
            [
                {"$match": {"username": username}},
                {
                    "$lookup": {
                        "from": "recipies",
                        "localField": "created_recipes.recipe_id",
                        "foreignField": "oid",
                        "as": "recipes",
                    }
                },
                {"$project": {"_id": 0, "recipes": 1}},
            ]
        )
        return await cursor.next()

    async def check_is_recipe_liked(self, username: str, recipe_id: str) -> bool:
        user = await self._collection.find_one(
            {"username": username, "liked_recipes": {"recipe_id": recipe_id}}
        )
        result = bool(user)
        logger.debug(result)
        return bool(user)

    async def check_is_author_of_recipe(self, username: str, recipe: Recipe) -> bool:
        user = await self._collection.find_one(
            {"username": username, "created_recipes": {"recipe_id": recipe.oid}}
        )
        return bool(user)
