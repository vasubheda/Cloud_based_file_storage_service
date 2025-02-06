from pydantic import BaseModel
from typing import Literal

class ComplaintCreateSchema(BaseModel):
    order_id: str
    product_id: str
    issue: str
    image_url: str | None = None

class ComplaintResponseSchema(BaseModel):
    id: str
    user_id: str
    order_id: str
    product_id: str
    issue: str
    image_url: str | None = None
    status: Literal["open", "rejected"]
