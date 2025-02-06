from fastapi import APIRouter, HTTPException
from ..usecases.auth.register import register_user
from ..models.schemas.user_schema import UserCreate, UserResponse
from ..models.domain.user import User
from ..utils.security import hash_password

router = APIRouter()

@router.post("/register", response_model=UserResponse)
async def register(user: UserCreate):
    hashed_pwd=hash_password(user.password)
    user_id = await register_user(User(name=user.name,email=user.email,password_hash=hashed_pwd, role=user.role))
    return {"id": str(user_id), "name": user.name, "email": user.email, "role": user.role}
