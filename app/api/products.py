from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app import schemas, crud

router = APIRouter(prefix="/products", tags=["Products"])


@router.post("/", response_model=schemas.ProductOut)
async def create_product(
    product: schemas.ProductCreate, db: AsyncSession = Depends(get_db)
):
    return await crud.crud_products.create_product(db, product)


@router.get("/", response_model=list[schemas.ProductOut])
async def get_all_products(db: AsyncSession = Depends(get_db)):
    return await crud.crud_products.get_products(db)


@router.get("/{product_id}", response_model=schemas.ProductOut)
async def get_product(product_id: int, db: AsyncSession = Depends(get_db)):
    product = await crud.crud_products.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.put("/{product_id}", response_model=schemas.ProductOut)
async def update_product(
    product_id: int,
    product_update: schemas.ProductUpdate,
    db: AsyncSession = Depends(get_db),
):
    updated = await crud.crud_products.update_product(db, product_id, product_update)
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated


@router.delete("/{product_id}")
async def delete_product(product_id: int, db: AsyncSession = Depends(get_db)):
    deleted = await crud.crud_products.delete_product(db, product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"detail": "Product deleted"}
