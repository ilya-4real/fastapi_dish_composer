from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="fastapi_proj/../.env",
        extra="ignore",
    )
    MONGO_USERNAME: str
    MONGO_PASSWORD: str
    MONGO_PORT: int
    MONGO_HOST: str
    CORS_ORIGINS: list[str]
    mongo_component_collection: str = Field(
        default="components", alias="MONGO_COMP_COLL"
    )
    MODE: Literal["DEV", "PROD"] = Field(default="PROD")
    mongo_recipe_collection: str = Field(default="recipies", alias="MONGO_REC_COLL")
    mongo_users_collection: str = Field(default="users", alias="MONGO_USERS_COLL")
    mongo_db_name: str = Field(default="dish", alias="MONGO_DB_NAME")

    @property
    def mongo_uri(self):
        return f"mongodb://{self.MONGO_USERNAME}:{self.MONGO_PASSWORD}@{self.MONGO_HOST}:{self.MONGO_PORT}"


settings = Settings()  # type: ignore
