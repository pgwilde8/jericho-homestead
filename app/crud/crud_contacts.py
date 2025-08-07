# crud_contacts.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import insert
from app.models.models import Contact
from app.schemas.contact import ContactCreate

async def create_contact(db: AsyncSession, contact: ContactCreate) -> Contact:
    new_contact = Contact(**contact.dict())
    db.add(new_contact)
    await db.commit()
    await db.refresh(new_contact)
    return new_contact

async def get_contacts(db: AsyncSession):
    result = await db.execute(select(Contact).order_by(Contact.created_at.desc()))
    return result.scalars().all()
