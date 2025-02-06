from beanie import Document
from typing import Literal
from bson import ObjectId
from datetime import datetime

class Complaint(Document):
    user_id: ObjectId
    order_id: ObjectId
    product_id: ObjectId
    issue: str
    image_url: str
    status: Literal["open", "rejected"]
    createdAt: datetime = datetime.utcnow()
    updatedAt: datetime = datetime.utcnow()

    class Settings:
        collection = "complaints"
