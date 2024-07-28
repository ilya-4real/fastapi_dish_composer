from fastapi_proj.logic.mediator import Mediator
from tests.mocks.commands import DummyCommand, DummyCommandFactory, DummyCommandHandler


def test_command_registration(test_container):
    mediator: Mediator = test_container.resolve(Mediator)
    handler = DummyCommandHandler()
    mediator.register_command(DummyCommand, [handler])
    handlers_from_mediator = mediator.commands_map[DummyCommand]
    assert handlers_from_mediator is not None
    assert isinstance(handlers_from_mediator[0], DummyCommandHandler)


async def test_correct_handler_called(test_container):
    mediator: Mediator = test_container.resolve(Mediator)
    handler = DummyCommandHandler()
    mediator.register_command(DummyCommand, [handler])
    command = DummyCommandFactory.build()
    result = await mediator.handle_command(command)
    assert command.command_text == result[0]
