import pytest

from config import parse_users, validate_config


def test_parse_users():
    assert parse_users("user1:pass1,user2:pass2") == {"user1": "pass1", "user2": "pass2"}


def test_parse_users_none():
    assert parse_users(None) == {}


@pytest.mark.parametrize("config_path, value", [
    ("config.AUTH_USERS", {}),
    ("config.SQLALCHEMY_DATABASE_URL", None),
])
def test_missing_environment_config(monkeypatch, config_path, value):
    monkeypatch.setattr(config_path, value)

    with pytest.raises(ValueError):
        validate_config()
