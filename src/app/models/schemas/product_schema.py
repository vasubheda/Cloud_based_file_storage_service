from pydantic import BaseModel
from typing import Optional,List

class ProductCreate(BaseModel):
    title: str
    description: str
    category: str
    price: float
    rating: Optional[float] = None
    brand: str
    images: List[str]
    thumbnail: str
    seller_id: str
    createdAt: str
    updatedAt: str