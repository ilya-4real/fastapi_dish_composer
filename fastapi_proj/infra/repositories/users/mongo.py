from dataclasses import dataclass

from fastapi_proj.infra.repositories.recipies.mongo import AbstractMongoRepository
from fastapi_proj.infra.repositories.users.base import BaseUserRepository


@dataclass
class MongoUserRepository(AbstractMongoRepository, BaseUserRepository):
    async def create_new(self, username: str) -> None:
        default_user = {
            "username": username,
            "liked_recipes": [],
            "created_recipes": [],
        }
        await self._collection.insert_one(default_user)

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
