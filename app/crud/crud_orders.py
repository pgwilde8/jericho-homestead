
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from app.models.order import Order
from app.schemas.order import OrderCreate, OrderUpdate

async def create_order(db: AsyncSession, order_in: OrderCreate) -> Order:
    new_order = Order(**order_in.dict())
    db.add(new_order)
    await db.commit()
    await db.refresh(new_order)
    return new_order

async def get_order(db: AsyncSession, order_id: int) -> Order | None:
    result = await db.execute(select(Order).where(Order.id == order_id))
    return result.scalar_one_or_none()

async def get_orders(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Order]:
    result = await db.execute(select(Order).offset(skip).limit(limit))
    return result.scalars().all()

async def update_order(db: AsyncSession, order_id: int, order_in: OrderUpdate) -> Order | None:
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if order:
        for field, value in order_in.dict(exclude_unset=True).items():
            setattr(order, field, value)
        await db.commit()
        await db.refresh(order)
    return order

async def delete_order(db: AsyncSession, order_id: int) -> bool:
    result = await db.execute(select(Order).where(Order.id == order_id))
    order = result.scalar_one_or_none()
    if order:
        await db.delete(order)
        await db.commit()
        return True
    return False
