import sys

from fastapi import FastAPI
from loguru import logger
import uvicorn

from api.api_v1.api import api_router
from config import LOG_LEVEL, LOG_AS_JSON, OPEN_API_TAGS
from models import models
from models.database import engine


def setup_logging():
    logger.remove()
    is_debug = LOG_LEVEL == "DEBUG"
    logger.add(
        sys.stdout, colorize=False, level=LOG_LEVEL,
        serialize=LOG_AS_JSON,
        backtrace=is_debug, diagnose=is_debug
    )


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="GyroLogServer", openapi_tags=OPEN_API_TAGS)

app.include_router(api_router, prefix="/V1")


if __name__ == "__main__":
    setup_logging()
    uvicorn.run(app, host="0.0.0.0", port=8000)