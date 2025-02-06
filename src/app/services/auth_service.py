from fastapi import HTTPException
from app.repositories.user_repository import UserRepository
from app.utils.security import verify_password, create_jwt_token
from app.models.schemas.user_schema import LoginRequest, LoginResponse
from motor.motor_asyncio import AsyncIOMotorDatabase

class AuthService:
    @staticmethod
    async def authenticate_user(data: LoginRequest, db: AsyncIOMotorDatabase):
        user = await UserRepository.get_user_by_email(data.email, db)

        if not user or not verify_password(data.password, user["password_hash"]):
            raise HTTPException(status_code=401, detail="Invalid email or password")

        token = create_jwt_token({"user_id": str(user["_id"]), "role": user["role"]})
        return LoginResponse(access_token=token, token_type="bearer")