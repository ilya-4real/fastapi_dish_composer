from fastapi_proj.database import BeanieRepository
from fastapi_proj.recipies.models import Recipe


class RecipeRepository(BeanieRepository):
    model = Recipe

    async def add_recipe(self, recipe: Recipe):
        await recipe.insert()