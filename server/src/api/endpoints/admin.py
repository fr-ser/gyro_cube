from fastapi import APIRouter, Depends, HTTPException, status
from loguru import logger
from sqlalchemy.orm import Session

from models.database import get_db
from api.authentication import authenticate


router = APIRouter()


@router.get("/health", tags=["admin"], status_code=status.HTTP_204_NO_CONTENT)
def check_health(db: Session = Depends(get_db), is_user_valid: bool = Depends(authenticate)):
    """
        Check Health
    """

    try:
        db.execute("SELECT 1;")
    except Exception:
        logger.exception("Health Check error")
        raise HTTPException(status_code=500, detail="Database Problem")
