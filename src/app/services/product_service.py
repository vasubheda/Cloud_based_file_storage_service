from bson import ObjectId
from ..repositories.product_repository import ProductRepository
from ..models.domain.product import Product

class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    async def get_product(self, product_id: ObjectId) -> Product:
        return await self.product_repository.get_product_by_id(product_id)