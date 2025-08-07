from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

async def get_user(db: AsyncSession, user_id: int):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalars().first()

async def get_all_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()

async def create_user(db: AsyncSession, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def update_user(db: AsyncSession, user_id: int, user_update: UserUpdate):
    await db.execute(update(User).where(User.id == user_id).values(**user_update.dict()))
    await db.commit()
    return await get_user(db, user_id)

async def delete_user(db: AsyncSession, user_id: int):
    await db.execute(delete(User).where(User.id == user_id))
    await db.commit()
    return {"msg": "User deleted"}