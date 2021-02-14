import secrets


from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import config


security = HTTPBasic()


def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    """
    Use BasicAuth to authenticate
    """

    if credentials.username in config.AUTH_USERS and secrets.compare_digest(
        credentials.password, config.AUTH_USERS[credentials.username]
    ):
        return True

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid"
    )
