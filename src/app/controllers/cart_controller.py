from fastapi import HTTPException
from bson import ObjectId
from ..models.schemas.cart_schema import CartItemCreate, CartItemResponse
from ..usecases.cart.add_to_cart import AddToCartUseCase

class CartController:
    def __init__(self):
        self.add_to_cart_usecase = AddToCartUseCase()

    async def add_to_cart(
        self,
        cart_item: CartItemCreate,
        user_id: ObjectId
    ) -> CartItemResponse:
        try:
            cart_item = await self.add_to_cart_usecase.execute(cart_item, user_id)
            return CartItemResponse(**cart_item.dict())
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail="Internal server error")