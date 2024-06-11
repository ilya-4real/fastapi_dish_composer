import logging
from contextlib import asynccontextmanager
from logging import getLogger

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from fastapi_proj.application.components.handlers import router as component_router
from fastapi_proj.application.recipies.handlers import router as recipe_router
from fastapi_proj.application.users.handlers import router as users_router
from fastapi_proj.config import settings
from fastapi_proj.domain.exceptions.base import ApplicationException

logger = getLogger(__name__)


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

logger.debug(settings.CORS_ORIGINS)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(ApplicationException)
async def handle_application_exception(request: Request, exc: ApplicationException):
    return JSONResponse(content={"error": exc.message}, status_code=exc.status_code)


app.include_router(component_router)
app.include_router(recipe_router)
app.include_router(users_router)
