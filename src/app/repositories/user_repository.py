from app.config.database import get_database

async def create_user(user_data: dict):
    db = get_database()
    user_collection = db["users"]
    new_user = await user_collection.insert_one(user_data)
    return new_user.inserted_id