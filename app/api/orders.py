from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app import schemas
from app.crud import crud_orders
from app.db.session import get_db

router = APIRouter()

# Create a new order
@router.post("/", response_model=schemas.OrderOut)
async def create_order(order: schemas.OrderCreate, db: AsyncSession = Depends(get_db)):
    return await crud_orders.create_order(db, order)

# Get all orders
@router.get("/", response_model=List[schemas.OrderOut])
async def get_orders(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await crud_orders.get_orders(db, skip=skip, limit=limit)

# Get a single order by ID
@router.get("/{order_id}", response_model=schemas.OrderOut)
async def get_order(order_id: int, db: AsyncSession = Depends(get_db)):
    db_order = await crud_orders.get_order(db, order_id)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

# Update an order
@router.put("/{order_id}", response_model=schemas.OrderOut)
async def update_order(order_id: int, order: schemas.OrderUpdate, db: AsyncSession = Depends(get_db)):
    db_order = await crud_orders.update_order(db, order_id, order)
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return db_order

# Delete an order
@router.delete("/{order_id}")
async def delete_order(order_id: int, db: AsyncSession = Depends(get_db)):
    success = await crud_orders.delete_order(db, order_id)
    if not success:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"detail": "Order deleted"}
