from dataclasses import dataclass

from fastapi_proj.domain.enteties.base import BaseEntity
from fastapi_proj.domain.enteties.component import Component


@dataclass
class Recipe(BaseEntity):
    title: str
    description: str
    components: list[Component]
