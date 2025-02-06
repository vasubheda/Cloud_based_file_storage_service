from pydantic import BaseModel
from typing import List, Literal

class OrderItemSchema(BaseModel):
    product_id: str
    quantity: int
    price: float

class OrderCreateSchema(BaseModel):
    items: List[OrderItemSchema]

class OrderResponseSchema(BaseModel):
    id: str
    user_id: str
    items: List[OrderItemSchema]
    total_amount: float
    status: Literal["pending", "shipped", "delivered", "cancelled"]
