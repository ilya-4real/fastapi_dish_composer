import pytest
from punq import Container, Scope

from fastapi_proj.logic.mediator import Mediator


@pytest.fixture
def empty_mediator():
    return Mediator()


@pytest.fixture
def test_container(empty_mediator) -> Container:
    container = Container()
    container.register(Mediator, instance=empty_mediator, scope=Scope.singleton)
    return container
