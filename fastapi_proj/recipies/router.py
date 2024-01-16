from fastapi.routing import APIRouter
from fastapi_proj.recipies.models import Recipe
from fastapi_proj.recipies.repo import RecipeRepository


RecipeRouter = APIRouter(prefix='/recipe')


@RecipeRouter.get('/get_recipe{id}', tags=['recipes'])
async def get_recipe(id: str):
    return {'responce': 'Here is recepe'}


@RecipeRouter.post('/add_recipe', tags=['recipes'])
async def add_recipe(recipe: Recipe):
    repo = RecipeRepository()
    await repo.add_recipe(recipe)
    # print(recipe.model_dump())
    return {'responce': 'Recipe added'}
