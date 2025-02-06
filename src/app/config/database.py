from motor.motor_asyncio import AsyncIOMotorClient
from .settings import settings

# Initialize MongoDB Client
client = AsyncIOMotorClient(settings.MONGO_DB_URL)

# Select Database
database = client[settings.MONGO_DB_NAME]

# Function to get the database instance
def get_database():
    return database
