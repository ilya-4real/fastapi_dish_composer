from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_proj import RecipeRouter, AuthRouter, CompoundRouter
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from contextlib import asynccontextmanager

from fastapi_proj.config import MONGO_URI
from fastapi_proj import models

origins = [
    "http://localhost:3000",
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(MONGO_URI)
    client = AsyncIOMotorClient(MONGO_URI)
    await init_beanie(database=client.db_name, document_models=models)
    print("Startup complete")
    yield
    print("Shotdown complete")


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(RecipeRouter)
app.include_router(AuthRouter)
app.include_router(CompoundRouter)
