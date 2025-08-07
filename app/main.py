from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

# Import routers
from app.api import test_db
from app.api import users
from app.api import products
from app.api import orders
from app.api import donations
from app.api import contacts
from app.api import pages
from app.api import stripe

app = FastAPI(
    title="Jericho Homestead API",
    version="1.0.0"
)

# Mount static files
static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Mount routers
app.include_router(pages.router, tags=["pages"])  # Pages router should be first to handle root path
app.include_router(test_db.router, prefix="/test-db", tags=["test"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(products.router, prefix="/products", tags=["products"])
app.include_router(orders.router, prefix="/orders", tags=["orders"])
app.include_router(donations.router, prefix="/donations", tags=["donations"])
app.include_router(contacts.router, prefix="/contacts", tags=["contacts"])
app.include_router(stripe.router, prefix="/api", tags=["stripe"])  # Added Stripe routes
