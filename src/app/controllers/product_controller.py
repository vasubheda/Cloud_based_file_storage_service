from fastapi import APIRouter, Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.config.database import database
from app.usecases.products.preload_products import preload_products_usecase

router = APIRouter()

@router.post("/preload-products/", status_code=201)
async def preload_products(db: AsyncIOMotorDatabase = Depends(lambda: database)):
    """API Endpoint to preload products from DummyJSON."""
    return await preload_products_usecase(db)
