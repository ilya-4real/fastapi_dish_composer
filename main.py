from fastapi import FastAPI
from fastapi_proj import RecipeRouter
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from contextlib import asynccontextmanager

from fastapi_proj.config import MONGO_URI
from fastapi_proj import models


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = AsyncIOMotorClient(MONGO_URI)
    await init_beanie(database=client.db_name, document_models=models)
    print("Startup complete")
    yield
    print("Shotdown complete")


app = FastAPI(lifespan=lifespan)
    

app.include_router(RecipeRouter)
