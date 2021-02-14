import sys

from fastapi import FastAPI
from loguru import logger
from starlette.responses import RedirectResponse
import uvicorn

from api.api import api_router
from config import validate_config, LOG_LEVEL, LOG_AS_JSON, OPEN_API_TAGS
from models import models
from models.database import engine


def setup_logging():
    logger.remove()
    is_debug = LOG_LEVEL == "DEBUG"
    logger.add(
        sys.stdout,
        colorize=False,
        level=LOG_LEVEL,
        serialize=LOG_AS_JSON,
        backtrace=is_debug,
        diagnose=is_debug,
    )


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="GyroLogServer", openapi_tags=OPEN_API_TAGS)

app.include_router(api_router)


@app.get("/", include_in_schema=False)
async def home_redirect():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    validate_config()
    setup_logging()
    uvicorn.run(app, host="0.0.0.0", port=8000)
