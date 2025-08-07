from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.session import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    full_name = Column(String, nullable=False)


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    image_url = Column(String(255))
    stripe_product_id = Column(String(100))
    stripe_price_id = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)


class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)  # Made nullable for guest checkouts
    total_amount = Column(Float, nullable=False)
    shipping_name = Column(String(100), nullable=True)
    shipping_address = Column(Text, nullable=True)
    email = Column(String(100), nullable=True)
    stripe_session_id = Column(String(100), nullable=True)
    status = Column(String(50), default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("User")


class Donation(Base):
    __tablename__ = "donations"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    amount = Column(Float, nullable=False)
    message = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    user = relationship("User")


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    message = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
