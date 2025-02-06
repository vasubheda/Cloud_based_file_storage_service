from fastapi import HTTPException
from app.services.auth_service import AuthService
from app.models.schemas.user_schema import LoginRequest
from motor.motor_asyncio import AsyncIOMotorDatabase

class LoginUsecase:
    @staticmethod
    async def execute(data: LoginRequest, db: AsyncIOMotorDatabase):
        return await AuthService.authenticate_user(data, db)
