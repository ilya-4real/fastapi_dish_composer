from fastapi_proj.recipies.router import RecipeRouter
from fastapi_proj.auth.router import router as AuthRouter
from fastapi_proj.recipe_compose.router import router as CompoundRouter

from fastapi_proj.recipies.models import Recipe
from fastapi_proj.auth.models import User

from fastapi_proj.recipe_compose.models import GarnishORM, SauceORM, MeatORM

models = [Recipe, User, GarnishORM, SauceORM, MeatORM]
