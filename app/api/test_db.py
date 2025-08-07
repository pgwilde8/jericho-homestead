from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.user import UserCreate
from app.crud import crud_users

router = APIRouter(prefix="/test-db", tags=["Database Test"])

@router.post("/create-user")
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await crud_users.create_user(db, user)
    return db_user
