import pytest

from fastapi_proj.auth.utils import generate_jwt


@pytest.mark.parametrize(
    "username, id, exp_in_seconds, crypted_token",
    [
        ("", "-1324", -2 * 60, None),
        ("sdfasdf", "asdfs1324", -2 * 60, None),
    ],
)
def test_jwt_generation(username, id, exp_in_seconds, crypted_token):
    assert generate_jwt(username, id, exp_in_seconds) == crypted_token
