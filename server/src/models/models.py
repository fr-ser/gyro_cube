from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class GyroLog(Base):
    __tablename__ = "gyro_logs"

    timestamp = Column(Integer, primary_key=True, index=True)
    side = Column(Integer)
    side_timestamp = Column(Integer, ForeignKey("gyro_sides.timestamp"))

    sides = relationship("GyroSide")


class GyroSide(Base):
    __tablename__ = "gyro_sides"

    timestamp = Column(Integer, primary_key=True, index=True)
    side = Column(Integer)
    name = Column(String)
