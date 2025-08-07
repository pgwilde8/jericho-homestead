from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.db.session import get_db
from app import schemas
from app.crud import crud_users

router = APIRouter()

@router.post("/", response_model=schemas.UserOut)
async def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    return await crud_users.create_user(db=db, user=user)

@router.get("/{user_id}", response_model=schemas.UserOut)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    db_user = await crud_users.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/", response_model=List[schemas.UserOut])
async def get_users(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    users = await crud_users.get_all_users(db=db)
    return users[skip:skip + limit]

@router.put("/{user_id}", response_model=schemas.UserOut)
async def update_user(user_id: int, user: schemas.UserUpdate, db: AsyncSession = Depends(get_db)):
    db_user = await crud_users.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return await crud_users.update_user(db=db, user_id=user_id, user_update=user)

@router.delete("/{user_id}")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    db_user = await crud_users.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    await crud_users.delete_user(db=db, user_id=user_id)
    return {"message": "User deleted successfully"}
