import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from fastapi_proj.application.components.handlers import router as recipe_handler
from fastapi_proj.domain.exceptions.base import ApplicationException


@asynccontextmanager
async def lifespan(app: FastAPI):
    queue_handler = logging.getHandlerByName("queue_handler")
    queue_handler.listener.start()  # type: ignore
    yield
    queue_handler.listener.stop()  # type: ignore


app = FastAPI(
    debug=True,
    title="Dish builder",
    description="API that provides info about different dishes and their composition",
    lifespan=lifespan,
)


@app.exception_handler(ApplicationException)
async def handle_application_exception(request: Request, exc: ApplicationException):
    return JSONResponse(content={"error": exc.message}, status_code=exc.status_code)


app.include_router(recipe_handler)
