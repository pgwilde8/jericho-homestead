from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app import schemas
from app.crud import crud_contacts
from app.db.session import get_db

router = APIRouter()

# Create a new contact form submission
@router.post("/", response_model=schemas.ContactOut)
async def create_contact(contact: schemas.ContactCreate, db: AsyncSession = Depends(get_db)):
    return await crud_contacts.create_contact(db, contact)

# Get all contact form submissions
@router.get("/", response_model=List[schemas.ContactOut])
async def get_contacts(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await crud_contacts.get_contacts(db, skip=skip, limit=limit)

# Get a single contact by ID
@router.get("/{contact_id}", response_model=schemas.ContactOut)
async def get_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    db_contact = await crud_contacts.get_contact(db, contact_id)
    if not db_contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact

# Delete a contact
@router.delete("/{contact_id}")
async def delete_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    success = await crud_contacts.delete_contact(db, contact_id)
    if not success:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"detail": "Contact deleted"}
