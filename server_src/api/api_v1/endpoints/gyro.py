from fastapi import APIRouter, Depends
from fastapi_pagination import pagination_params, Page
from fastapi_pagination.paginator import paginate
from sqlalchemy.orm import Session

from api.authentication import authenticate
from models.database import get_db
from models import schemas, crud


router = APIRouter()


@router.get("/logs", response_model=Page[schemas.GyroLog],
            dependencies=[Depends(pagination_params)])
def read_logs(db: Session = Depends(get_db), is_user_valid: bool = Depends(authenticate),
              skip: int = 0, limit: int = 100,):
    """
    Retrieve gyro_logs.
    """

    gyro_logs = crud.get_gyro_logs(db, skip=skip, limit=limit)

    return paginate(gyro_logs)


@router.get("/sides", response_model=Page[schemas.GyroSide],
            dependencies=[Depends(pagination_params)])
def read_side_names(db: Session = Depends(get_db), is_user_valid: bool = Depends(authenticate),
                    skip: int = 0, limit: int = 100,):
    """
    Retrieve gyro_side_names.
    """

    gyro_side_names = crud.get_gyro_side_names(db, skip=skip, limit=limit)

    return paginate(gyro_side_names)


@router.post("/sides", response_model=schemas.GyroSide)
def create_side_names(side_name: schemas.GyroSideCreate, db: Session = Depends(get_db),
                      is_user_valid: bool = Depends(authenticate)):
    """
    Create gyro_side_names.
    """
    return crud.create_gyro_side_name(db, side_name)


@router.post("/logs", response_model=schemas.GyroLog)
def create_log(log: schemas.GyroLogCreate, db: Session = Depends(get_db),
               is_user_valid: bool = Depends(authenticate)):
    """
    Create gyro_logs.
    """
    return crud.create_gyro_log(db, log)
