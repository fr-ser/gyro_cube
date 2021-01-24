import os


LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
LOG_AS_JSON = bool(int(os.environ.get("LOG_AS_JSON", "0")))

OPEN_API_TAGS = [
    {
        "name": "admin",
        "description": "Administrative Tasks like checking health",
    },
    {
        "name": "gyro",
        "description": "Gyro Cube endpoints"
    },
]


def parse_users(auth_users):
    """
    in the ENV we expect a string like
        "user:password,new_user:new_password"
    :return: dict with usernames as keys and passwords as values
    """
    env_content = os.environ.get("AUTH_USERS")
    if not env_content:
        return {}

    return dict([i.split(":") for i in env_content.split(',')])


AUTH_USERS = parse_users(os.environ["AUTH_USERS"])

SQLALCHEMY_DATABASE_URL = os.environ["SQLALCHEMY_DATABASE_URL"]
