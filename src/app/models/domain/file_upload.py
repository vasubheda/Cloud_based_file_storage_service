from beanie import Document
from typing import Literal
from bson import ObjectId
from datetime import datetime

class FileUpload(Document):
    user_id: ObjectId
    file_url: str
    file_type: Literal["product", "complaint"]
    createdAt: datetime = datetime.utcnow()
    updatedAt: datetime = datetime.utcnow()

    class Settings:
        collection = "files"
