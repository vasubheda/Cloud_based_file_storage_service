from app.config.database import get_database
from motor.motor_asyncio import AsyncIOMotorDatabase

class UserRepository:
    
    @staticmethod
    async def create_user(user_data: dict):
        db = get_database()
        user_collection = db["users"]
        new_user = await user_collection.insert_one(user_data)
        return new_user.inserted_id


    @staticmethod
    async def get_user_by_email(email: str, db: AsyncIOMotorDatabase):
        return await db["users"].find_one({"email": email})