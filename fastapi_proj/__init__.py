from fastapi_proj.recipies.router import RecipeRouter
from fastapi_proj.auth.router import router as AuthRouter

from fastapi_proj.recipies.models import Recipe
from fastapi_proj.auth.models import User

models = [Recipe, User]
