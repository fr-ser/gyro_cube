from pydantic import BaseModel, Field, BaseConfig


class BaseSchema(BaseModel):
    class Config(BaseConfig):
        allow_population_by_field_name = True


class GyroSideBase(BaseSchema):
    timestamp: int
    side: int = Field(..., gt=-1, lt=7)
    name: str


class GyroSideCreate(GyroSideBase):
    pass


class GyroSide(GyroSideBase):
    class Config:
        orm_mode = True


class GyroLogBase(BaseSchema):
    timestamp: int
    side: int = Field(..., gt=-1, lt=7)


class GyroLogCreate(GyroLogBase):
    pass


class GyroLog(GyroLogBase):
    sides: GyroSide

    class Config:
        orm_mode = True
