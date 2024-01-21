from fastapi_proj.auth.utils import generate_jwt


def test_jwt_generation():
    token = generate_jwt("random", "1334sa", 5 * 60)
    ...
