import time

from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func

from . import models, schemas


def get_gyro_log(db: Session, timestamp: int):
    return (
        db.query(models.GyroLog).filter(models.GyroLog.timestamp == timestamp).first()
    )


def get_gyro_logs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.GyroLog).offset(skip).limit(limit).all()


def create_gyro_log(db: Session, side: int):
    most_recent_ts = (
        db.query(func.max(models.GyroSide.timestamp))
        .filter(models.GyroSide.side == side)
        .scalar()
    )

    db_gyro_log = models.GyroLog(
        side=side, side_timestamp=most_recent_ts, timestamp=int(time.time())
    )

    db.add(db_gyro_log)
    db.commit()
    return db_gyro_log


def get_current_gyro_side_name(db: Session):
    return db.query(models.GyroSide).order_by(models.GyroSide.timestamp.desc()).first()


def get_gyro_side_name(db: Session, timestamp: int):
    return (
        db.query(models.GyroSide).filter(models.GyroSide.timestamp == timestamp).first()
    )


def get_gyro_side_names(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.GyroSide).offset(skip).limit(limit).all()


def create_gyro_side_name(db: Session, side_name: schemas.GyroSide):
    db_gyro_side_name = models.GyroSide(**side_name.dict())
    db.add(db_gyro_side_name)
    db.commit()
    return db_gyro_side_name
