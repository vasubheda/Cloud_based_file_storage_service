from beanie import Document
from bson import ObjectId
from datetime import datetime

class CartItem(Document):
    user_id: ObjectId
    product_id: ObjectId
    quantity: int
    createdAt: datetime = datetime.utcnow()
    updatedAt: datetime = datetime.utcnow()

    class Settings:
        collection = "cart"
