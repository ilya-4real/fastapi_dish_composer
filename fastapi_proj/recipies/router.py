from fastapi.routing import APIRouter
from fastapi_proj.recipies.models import Recipe


RecipeRouter = APIRouter(prefix='/recipe')


@RecipeRouter.get('/get_recipe{id}', tags=['recipes'])
async def get_recipe(id: str):
    return {'responce': 'Here is recepe'}


@RecipeRouter.post('/add_recipe', tags=['recipes'])
async def add_recipe(recipe: Recipe):
    return {'responce': 'Recipe added'}
