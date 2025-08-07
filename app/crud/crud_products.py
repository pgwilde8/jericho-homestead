from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


async def get_product(db: AsyncSession, product_id: int):
    result = await db.execute(select(Product).where(Product.id == product_id))
    return result.scalars().first()


async def get_products(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Product).offset(skip).limit(limit))
    return result.scalars().all()


async def create_product(db: AsyncSession, product: ProductCreate):
    db_product = Product(**product.dict())
    db.add(db_product)
    await db.commit()
    await db.refresh(db_product)
    return db_product


async def update_product(db: AsyncSession, product_id: int, product: ProductUpdate):
    result = await db.execute(select(Product).where(Product.id == product_id))
    db_product = result.scalars().first()
    if db_product is None:
        return None
    for key, value in product.dict(exclude_unset=True).items():
        setattr(db_product, key, value)
    await db.commit()
    await db.refresh(db_product)
    return db_product


async def delete_product(db: AsyncSession, product_id: int):
    result = await db.execute(select(Product).where(Product.id == product_id))
    db_product = result.scalars().first()
    if db_product is None:
        return None
    await db.delete(db_product)
    await db.commit()
    return db_product
