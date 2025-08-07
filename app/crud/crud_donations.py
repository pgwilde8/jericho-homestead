# crud_donations.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import insert
from app.models.models import Donation
from app.schemas.donation import DonationCreate

async def create_donation(db: AsyncSession, donation: DonationCreate) -> Donation:
    new_donation = Donation(**donation.dict())
    db.add(new_donation)
    await db.commit()
    await db.refresh(new_donation)
    return new_donation

async def get_donations(db: AsyncSession):
    result = await db.execute(select(Donation).order_by(Donation.created_at.desc()))
    return result.scalars().all()



