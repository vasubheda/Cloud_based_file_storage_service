from fastapi import APIRouter, HTTPException, Depends
from app.usecases.auth.login_usecase import LoginUsecase
from ..usecases.auth.register import register_user
from ..models.schemas.user_schema import UserCreate, UserResponse, LoginRequest, LoginResponse
from ..models.domain.user import User
from ..utils.security import hash_password
from app.config.database import get_database
from motor.motor_asyncio import AsyncIOMotorDatabase

router = APIRouter()

@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate):
    hashed_pwd=hash_password(user.password)
    user_id = await register_user(User(name=user.name,email=user.email,password_hash=hashed_pwd, role=user.role))
    return {"id": str(user_id), "name": user.name, "email": user.email, "role": user.role}

@router.post("/login", response_model=LoginResponse)
async def login(data: LoginRequest, db: AsyncIOMotorDatabase = Depends(get_database)):
    return await LoginUsecase.execute(data, db)
