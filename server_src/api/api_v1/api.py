from fastapi import APIRouter

from api.api_v1.endpoints import admin, gyro

api_router = APIRouter()
api_router.include_router(admin.router, prefix="/admin", tags=["admin"])
api_router.include_router(gyro.router, prefix="/gyro", tags=["gyro"])
