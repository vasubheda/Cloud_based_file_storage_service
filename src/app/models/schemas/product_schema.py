# from pydantic import BaseModel
# from typing import List

# class ProductCreateSchema(BaseModel):
#     title: str
#     description: str
#     category: str
#     price: float
#     rating: float
#     brand: str
#     images: List[str]
#     thumbnail: str

# class ProductResponseSchema(ProductCreateSchema):
#     id: str
#     seller_id: str

# class ProductUpdateSchema(BaseModel):
#     title: str | None = None
#     description: str | None = None
#     category: str | None = None
#     price: float | None = None
#     rating: float | None = None
#     brand: str | None = None
#     images: List[str] | None = None
#     thumbnail: str | None = None

from pydantic import BaseModel

class ProductCreate(BaseModel):
    title: str
    description: str
    category: str
    price: float
    rating: float
    brand: str
    images: list[str]
    thumbnail: str