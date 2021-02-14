import pytest

from config import parse_users, validate_config


def test_parse_users():
    assert parse_users("user1:pass1,user2:pass2") == {"user1": "pass1", "user2": "pass2"}


def test_parse_users_none():
    assert parse_users(None) == {}


@pytest.mark.parametrize("env", ["AUTH_USERS", "SQLALCHEMY_DATABASE_URL"])
def test_missing_environment_config_production(monkeypatch, env):
    monkeypatch.setattr("config.ENVIRONMENT", "production")
    monkeypatch.delenv(env, raising=False)

    with pytest.raises(ValueError):
        validate_config()


def test_missing_environment_config_development(monkeypatch):
    monkeypatch.setattr("config.ENVIRONMENT", "development")

    monkeypatch.delenv("AUTH_USERS", raising=False)
    monkeypatch.delenv("SQLALCHEMY_DATABASE_URL", raising=False)

    validate_config()
