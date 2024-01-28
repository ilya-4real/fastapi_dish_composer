from fastapi import HTTPException, APIRouter, status
from fastapi_proj.recipies.models import Recipe, RecipeDTO


RecipeRouter = APIRouter(prefix="/recipe", tags=["recipes"])


@RecipeRouter.get("/{id}/get")
async def get_recipe(id: str):
    return {"responce": "Here is recepe"}


@RecipeRouter.post("/")
async def add_recipe(recipe: RecipeDTO):
    new_recipe = Recipe(title=recipe.title)
    await new_recipe.insert()  # type: ignore


@RecipeRouter.post("/{id}/update")
async def update_recipe(id: str, recipe: RecipeDTO):
    found = await Recipe.find_one({"id": id})
    if not found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="recipe not found"
        )
    await found.set(**recipe.model_dump())
