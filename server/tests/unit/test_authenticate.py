from fastapi import HTTPException
from fastapi.security import HTTPBasicCredentials
import pytest

from api.authentication import authenticate


def test_can_authenticate(monkeypatch):
    monkeypatch.setattr("config.AUTH_USERS", {"my_user": "my_password"})
    credentials = HTTPBasicCredentials(username="my_user", password="my_password")

    assert authenticate(credentials) is True


def test_can_not_authenticate_when_no_users_provided(monkeypatch):
    monkeypatch.setattr("config.AUTH_USERS", {})
    credentials = HTTPBasicCredentials(username="user", password="pass")

    with pytest.raises(HTTPException) as exception:
        authenticate(credentials)

    assert exception.value.status_code == 401


def test_can_not_authenticate_with_wrong_password(monkeypatch):
    monkeypatch.setattr("config.AUTH_USERS", {"abc": "def"})
    credentials = HTTPBasicCredentials(username="abc", password="not_def")

    with pytest.raises(HTTPException) as exception:
        authenticate(credentials)

    assert exception.value.status_code == 401


@pytest.mark.parametrize(
    "user,password",
    [
        ["", ""],
        [None, None]
    ]
)
def test_can_not_authenticate_with_empty_credentials(monkeypatch, user, password):
    monkeypatch.setattr("config.AUTH_USERS", {"abc": "def"})
    credentials = HTTPBasicCredentials(username="", password="")

    with pytest.raises(HTTPException) as exception:
        authenticate(credentials)

    assert exception.value.status_code == 401
