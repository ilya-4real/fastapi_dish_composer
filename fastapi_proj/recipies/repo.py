from fastapi_proj.database import BeanieRepository
from fastapi_proj.recipies.schemas import RecipeDTO
from fastapi_proj.recipies.models import Recipe


class RecipeRepository(BeanieRepository):
    model = Recipe

    async def add_recipe(self, recipe: RecipeDTO):
        new_recipe = self.model(**recipe.model_dump())
        await self.model.insert_one(new_recipe)
