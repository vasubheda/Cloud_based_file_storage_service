from beanie import Document
from typing import List, Literal
from bson import ObjectId
from datetime import datetime

class OrderItem:
    product_id: ObjectId
    quantity: int
    price: float

class Order(Document):
    user_id: ObjectId
    items: List[OrderItem]
    total_amount: float
    status: Literal["pending", "shipped", "delivered", "cancelled"]
    createdAt: datetime = datetime.utcnow()
    updatedAt: datetime = datetime.utcnow()

    class Settings:
        collection = "orders"
