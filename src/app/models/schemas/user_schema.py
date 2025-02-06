# from pydantic import BaseModel, EmailStr
# from typing import Literal

# class UserCreate(BaseModel):
#     name: str
#     email: EmailStr
#     password: str
#     role: Literal["admin", "buyer", "seller"]

# class UserResponse(BaseModel):
#     id: str
#     name: str
#     email: EmailStr
#     role: Literal["admin", "buyer", "seller"]

# class UserLoginSchema(BaseModel):
#     email: EmailStr
#     password: str

# class UserRoleUpdateSchema(BaseModel):
#     role: Literal["admin", "buyer", "seller"]


from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str

class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    role: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"