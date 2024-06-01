from fastapi import FastAPI

from fastapi_proj.application.recipes.handlers import router as recipe_handler

app = FastAPI(
    debug=True,
    title="Dish builder",
    description="API that provides info about different dishes and their composition",
)


app.include_router(recipe_handler)
