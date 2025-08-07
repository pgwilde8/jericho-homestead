from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app import schemas
from app.crud import crud_donations
from app.db.session import get_db

router = APIRouter()

# Create a new donation
@router.post("/", response_model=schemas.DonationOut)
async def create_donation(donation: schemas.DonationCreate, db: AsyncSession = Depends(get_db)):
    return await crud_donations.create_donation(db, donation)

# Get all donations
@router.get("/", response_model=List[schemas.DonationOut])
async def get_donations(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await crud_donations.get_donations(db, skip=skip, limit=limit)

# Get a single donation by ID
@router.get("/{donation_id}", response_model=schemas.DonationOut)
async def get_donation(donation_id: int, db: AsyncSession = Depends(get_db)):
    db_donation = await crud_donations.get_donation(db, donation_id)
    if not db_donation:
        raise HTTPException(status_code=404, detail="Donation not found")
    return db_donation

# Update a donation
@router.put("/{donation_id}", response_model=schemas.DonationOut)
async def update_donation(donation_id: int, donation: schemas.DonationUpdate, db: AsyncSession = Depends(get_db)):
    db_donation = await crud_donations.update_donation(db, donation_id, donation)
    if not db_donation:
        raise HTTPException(status_code=404, detail="Donation not found")
    return db_donation

# Delete a donation
@router.delete("/{donation_id}")
async def delete_donation(donation_id: int, db: AsyncSession = Depends(get_db)):
    success = await crud_donations.delete_donation(db, donation_id)
    if not success:
        raise HTTPException(status_code=404, detail="Donation not found")
    return {"detail": "Donation deleted"}
