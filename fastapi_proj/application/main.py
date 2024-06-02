from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from fastapi_proj.application.recipes.handlers import router as recipe_handler
from fastapi_proj.domain.exceptions.base import ApplicationException

app = FastAPI(
    debug=True,
    title="Dish builder",
    description="API that provides info about different dishes and their composition",
)


@app.exception_handler(ApplicationException)
async def handle_application_exception(
    request: Request, exc: ApplicationException
):
    return JSONResponse(
        content={"error": exc.message}, status_code=exc.status_code
    )


app.include_router(recipe_handler)
