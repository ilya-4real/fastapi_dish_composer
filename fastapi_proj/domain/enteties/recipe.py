from dataclasses import dataclass, field

from fastapi_proj.domain.enteties.base import BaseEntity
from fastapi_proj.domain.enteties.component import Component


@dataclass
class Recipe(BaseEntity):
    author: str
    title: str
    description: str | None
    components: list[Component] = field(default_factory=list)
    likes: int = field(default=0)
