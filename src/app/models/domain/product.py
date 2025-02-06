# from beanie import Document
# from pydantic import Field
# from typing import List
# from datetime import datetime
# from bson import ObjectId

# class Product(Document):
#     title: str
#     description: str
#     category: str
#     price: float
#     rating: float = Field(ge=0, le=5)  # Rating should be between 0-5
#     brand: str
#     images: List[str]
#     thumbnail: str
#     seller_id: ObjectId
#     createdAt: datetime = datetime.utcnow()
#     updatedAt: datetime = datetime.utcnow()

#     class Settings:
#         collection = "products"

from typing import List
from pydantic import BaseModel
from datetime import datetime

class Product(BaseModel):
    title: str
    description: str
    category: str
    price: float
    rating: float
    brand: str
    images: List[str]
    thumbnail: str
    seller_id: str
    created_at: datetime=datetime.utcnow()
    updated_at: datetime=datetime.utcnow()