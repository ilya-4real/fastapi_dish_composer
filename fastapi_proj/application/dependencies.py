from typing import Annotated

from fastapi import Depends
from punq import Container

from fastapi_proj.infra.container import init_container
from fastapi_proj.logic.mediator import Mediator


def get_mediator(container: Annotated[Container, Depends(init_container)]) -> Mediator:
    mediator: Mediator = container.resolve(Mediator)  # type: ignore
    return mediator
