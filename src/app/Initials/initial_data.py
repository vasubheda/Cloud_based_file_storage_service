import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from datetime import datetime
from passlib.context import CryptContext
from ..config.settings import settings

# MONGO_URI = os.getenv("MONGO_URI")
# DB_NAME = os.getenv("DB_NAME")

client = AsyncIOMotorClient(settings.MONGO_DB_URL)
database = client[settings.MONGO_DB_NAME]

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Default seller users
SELLERS = [
    {
        "_id": i,  # Fixed IDs: 1, 2, 3, 4, 5
        "name": f"Seller {i}",
        "email": f"seller{i}@example.com",
        "password_hash": pwd_context.hash("password123"),  # Hashed password
        "role": "seller",
        "createdAt": datetime.utcnow(),
        "updatedAt": datetime.utcnow()
    }
    for i in range(1, 6)
]

async def preload_sellers():
    users_collection = database["users"]
    
    # Check if sellers exist
    existing_count = await users_collection.count_documents({"_id": {"$in": [1, 2, 3, 4, 5]}})
    
    if existing_count == 5:
        print("Sellers already exist, skipping insertion.")
        return

    # Insert missing sellers
    await users_collection.insert_many(SELLERS)
    print("Default sellers inserted successfully.")

# Run the preload function
async def main():
    await preload_sellers()
    client.close()