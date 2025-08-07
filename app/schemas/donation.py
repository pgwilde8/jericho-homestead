from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class DonationCreate(BaseModel):
    name: str
    email: EmailStr
    amount: float
    message: Optional[str] = None

class DonationOut(DonationCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class DonationUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    amount: Optional[float] = None
    message: Optional[str] = None
