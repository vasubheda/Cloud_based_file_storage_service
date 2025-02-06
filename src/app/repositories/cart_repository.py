from bson import ObjectId
from ..config.database import get_database
from ..models.domain.cart import CartItem
from datetime import datetime

class CartRepository:
    def __init__(self):
        self.db = get_database()
        self.collection = self.db.cart_items

    async def create_cart_item(self, cart_item_data: dict) -> CartItem:
        result = await self.collection.insert_one(cart_item_data)
        cart_item_data["_id"] = result.inserted_id
        return CartItem(**cart_item_data)

    async def get_cart_item(self, user_id: ObjectId, product_id: ObjectId) -> CartItem:
        cart_item = await self.collection.find_one({
            "user_id": user_id,
            "product_id": product_id
        })
        return CartItem(**cart_item) if cart_item else None

    async def update_cart_item_quantity(
        self,
        cart_item_id: ObjectId,
        quantity: int
    ) -> CartItem:
        cart_item = await self.collection.find_one_and_update(
            {"_id": cart_item_id},
            {"$set": {
                "quantity": quantity,
                "updated_at": datetime.utcnow()
            }},
            return_document=True
        )
        return CartItem(**cart_item) if cart_item else None