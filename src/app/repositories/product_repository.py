import random
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.models.domain.product import Product

class ProductRepository:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.db = db
        self.collection = db["products"]

    async def count_products(self) -> int:
        """Check if products already exist in the database."""
        return await self.collection.count_documents({})

    async def insert_products(self, products: list[dict]):
        """Insert multiple products into the database."""
        return await self.collection.insert_many(products)

    async def get_random_seller_id(self) -> str:
        """Generate a random seller ID (simulated from 1 to 5)."""
        return str(random.randint(1, 5))