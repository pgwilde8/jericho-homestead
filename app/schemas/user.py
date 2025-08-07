# app/schemas/user.py
from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr

class UserUpdate(UserCreate):
    pass

class UserOut(UserCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
