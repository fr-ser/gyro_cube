from pydantic import BaseModel, Field


class GyroSideBase(BaseModel):
    timestamp: int
    side: int = Field(..., gt=0, lt=5)
    name: str


class GyroSideCreate(GyroSideBase):
    pass


class GyroSide(GyroSideBase):
    class Config:
        orm_mode = True


class GyroLogBase(BaseModel):
    timestamp: int
    side: int = Field(..., gt=0, lt=5)


class GyroLogCreate(GyroLogBase):
    pass


class GyroLog(GyroLogBase):
    sides: GyroSide

    class Config:
        orm_mode = True
