from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class ProductCreate(ProductBase):
    pass



class ProductUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    price: Optional[float]
    quantity: Optional[int]


class ProductOut(ProductBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

        from pydantic import BaseModel
from typing import Optional



