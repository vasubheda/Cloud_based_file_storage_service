from bson import ObjectId
from ...models.schemas.cart_schema import CartItemCreate
from ...models.domain.cart import CartItem
from ...services.cart_service import CartService
from ...services.product_service import ProductService

class AddToCartUseCase:
    def __init__(self):
        self.cart_service = CartService()
        self.product_service = ProductService()

    async def execute(self, cart_item_data: CartItemCreate, user_id: ObjectId) -> CartItem:
        # Validate product exists
        product = await self.product_service.get_product(ObjectId(cart_item_data.product_id))
        if not product:
            raise ValueError("Product not found")

        # Check if product is already in cart
        existing_cart_item = await self.cart_service.get_cart_item(
            user_id,
            ObjectId(cart_item_data.product_id)
        )

        if existing_cart_item:
            # Update quantity if product already exists in cart
            new_quantity = existing_cart_item.quantity + cart_item_data.quantity
            return await self.cart_service.update_cart_item_quantity(
                existing_cart_item.id,
                new_quantity
            )
        else:
            # Create new cart item
            cart_item_dict = cart_item_data.dict()
            cart_item_dict["user_id"] = user_id
            cart_item_dict["product_id"] = ObjectId(cart_item_dict["product_id"])
            
            return await self.cart_service.create_cart_item(cart_item_dict)
