from pydantic import BaseModel

class CartItemSchema(BaseModel):
    product_id: str
    quantity: int

class CartResponseSchema(BaseModel):
    user_id: str
    items: list[CartItemSchema]
