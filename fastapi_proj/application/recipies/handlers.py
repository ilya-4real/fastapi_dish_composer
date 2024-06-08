from typing import Annotated

from fastapi import APIRouter, Depends
from punq import Container

from fastapi_proj.application.recipies.schemas import CreateRecipeSchema
from fastapi_proj.infra.container import init_container
from fastapi_proj.logic.mediator import Mediator

router = APIRouter(prefix="/recipies", tags=["recipies"])


def get_mediator(container: Annotated[Container, Depends(init_container)]) -> Mediator:
    mediator: Mediator = container.resolve(Mediator)  # type: ignore
    return mediator


@router.post("/")
async def create_recipe(
    recipe: CreateRecipeSchema, mediator: Annotated[Mediator, Depends(get_mediator)]
): ...


@router.get("/{recipe_id}")
async def get_recipe_detail(recipe_id: str): ...


@router.delete("/{recipe_id}")
async def delete_recipe(recipe_id: str): ...


@router.put("/{recipe_id}")
async def update_recipe(recipe_id: str): ...


@router.get("/random")
async def generate_random_recipe(): ...


@router.get("/popular")
async def get_popular_recipes(limit: int = 10, offset: int = 0): ...


@router.get("/own")
async def get_users_recipes(username: str, limit: int = 20, offset: int = 0): ...


@router.get("/liked")
async def get_users_liked_recipes(username: str, limit: int = 20, offset: int = 0): ...
