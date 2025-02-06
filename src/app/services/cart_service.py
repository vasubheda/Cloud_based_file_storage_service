from bson import ObjectId
from ..repositories.cart_repository import CartRepository
from ..models.domain.cart import CartItem

class CartService:
    def __init__(self):
        self.cart_repository = CartRepository()

    async def create_cart_item(self, cart_item_data: dict) -> CartItem:
        return await self.cart_repository.create_cart_item(cart_item_data)

    async def get_cart_item(self, user_id: ObjectId, product_id: ObjectId) -> CartItem:
        return await self.cart_repository.get_cart_item(user_id, product_id)

    async def update_cart_item_quantity(
        self,
        cart_item_id: ObjectId,
        quantity: int
    ) -> CartItem:
        return await self.cart_repository.update_cart_item_quantity(
            cart_item_id,
            quantity
        )