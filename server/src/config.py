import os

ENVIRONMENT = os.environ.get("ENVIRONMENT", "production")
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
LOG_AS_JSON = bool(int(os.environ.get("LOG_AS_JSON", "0")))

OPEN_API_TAGS = [
    {
        "name": "admin",
        "description": "Administrative Tasks like checking health",
    },
    {"name": "gyro", "description": "Gyro Cube endpoints"},
]


def parse_users(auth_users):
    """
    :param auth_users str: example "user:password,new_user:new_password"

    :return: dict with usernames as keys and passwords as values
    """
    if not auth_users:
        return {}

    return dict([i.split(":") for i in auth_users.split(",")])


AUTH_USERS = parse_users(os.environ.get("AUTH_USERS", "me:self,him:other"))

SQLALCHEMY_DATABASE_URL = os.environ.get(
    "SQLALCHEMY_DATABASE_URL", "sqlite:///local_dev.db"
)


def validate_config():
    """
    Checks that all required configurations are set.
    Using this in favor of os.environ[...] importing this module without
    errors, which makes testing easier
    """

    if ENVIRONMENT not in ("development", "testing"):
        for env in ["AUTH_USERS", "SQLALCHEMY_DATABASE_URL"]:
            if not os.environ.get(env):
                raise ValueError(f"Missing/Invalid configuration for '{env}'")
