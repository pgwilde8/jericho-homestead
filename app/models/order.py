from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.db.base import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer)
    total_price = Column(Float)
    customer_name = Column(String)
    customer_email = Column(String)
