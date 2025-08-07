# app/schemas/order.py

from pydantic import BaseModel
from typing import Optional

class OrderBase(BaseModel):
    product_id: int
    quantity: int
    customer_name: Optional[str] = None

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    product_id: Optional[int] = None
    quantity: Optional[int] = None
    customer_name: Optional[str] = None

class OrderOut(OrderBase):
    id: int
    created_at: str
    updated_at: Optional[str] = None

    class Config:
        from_attributes = True
