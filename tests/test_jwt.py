import pytest

from fastapi_proj.auth.utils import generate_jwt, decode_jwt


@pytest.mark.parametrize(
    "username, id, exp_in_seconds, crypted_token",
    [
        ("", "-1324", -2 * 60, None),
        ("sdfasdf", "asdfs1324", -2 * 60, None),
    ],
)
def test_generate_jwt(username, id, exp_in_seconds, crypted_token):
    if crypted_token:
        assert generate_jwt(username, id, exp_in_seconds) == crypted_token
    else:
        assert crypted_token is None


@pytest.mark.parametrize(
    "token, username, id, exp_time",
    [("asfasdf.asdfasdfaw2.adsfv423", "ilya", "asdf12", 20 * 60)],
)
def test_decode_jwt(token, username, id, exp_time):
    token_payload = decode_jwt(token)
    if token_payload:
        user_name = token_payload["username"]
        user_id = token_payload["id"]
        exp_t = token_payload["exp_time"]
        assert user_name == username and user_id == id and exp_t == exp_time
