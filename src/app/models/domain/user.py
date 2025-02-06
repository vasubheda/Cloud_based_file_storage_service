# from beanie import Document
# from pydantic import EmailStr
# from typing import Literal
# from datetime import datetime

# class User(Document):
#     name: str
#     email: EmailStr
#     password_hash: str
#     role: Literal["admin", "buyer", "seller"]
#     createdAt: datetime = datetime.utcnow()
#     updatedAt: datetime = datetime.utcnow()

#     class Settings:
#         collection = "users"

from typing import Literal
from pydantic import BaseModel, EmailStr
from datetime import datetime

class User(BaseModel):
    name: str
    email: EmailStr
    password_hash: str
    role: Literal["admin", "buyer", "seller"]
    created_at: datetime=datetime.utcnow()
    updated_at: datetime=datetime.utcnow()