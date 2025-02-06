from fastapi import APIRouter, Depends, HTTPException
from ..models.schemas.cart_schema import CartItemSchema, CartResponseSchema
from ..controllers.cart_controller import CartController
from ..utils.security import get_current_user
from ..models.domain.user import User

router = APIRouter(prefix="/cart", tags=["cart"])

@router.post("/add", response_model=CartResponseSchema)
async def add_to_cart(
    cart_item: CartItemSchema,
    current_user: User = Depends(get_current_user)
) -> CartResponseSchema:
    if current_user.role != "buyer":
        raise HTTPException(
            status_code=403,
            detail="Only buyers can add items to cart"
        )
    
    controller = CartController()
    return await controller.add_to_cart(cart_item, current_user.id)