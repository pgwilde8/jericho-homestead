# Jericho Homestead Database Documentation

## Overview
The Jericho Homestead application uses PostgreSQL with SQLAlchemy ORM for database management. The database is structured to handle:
- User management
- Shop products and orders
- Donations
- Contact form submissions

## Database Connection
```
DATABASE_URL=postgresql+asyncpg://postgres:Securepass@localhost/jericho_homestead
```

## Database Structure

### Models (app/models/models.py)
1. **Users**
   - Primary table for user management
   - Fields: id, email, name, is_donor, created_at
   - Relationships: One-to-many with Orders and Donations

2. **Products**
   - Shop merchandise inventory
   - Fields: id, name, description, price, image_url, created_at

3. **Orders**
   - Track shop purchases
   - Fields: id, user_id, total_amount, created_at
   - Foreign Key: user_id references users.id

4. **Donations**
   - Track donor contributions
   - Fields: id, user_id, amount, message, created_at
   - Foreign Key: user_id references users.id

5. **Contacts**
   - Store contact form submissions
   - Fields: id, name, email, message, created_at

### CRUD Operations (app/crud/)
- `crud_users.py`: User management operations
- `crud_products.py`: Product inventory management
- `crud_orders.py`: Order processing
- `crud_donations.py`: Donation handling
- `crud_contacts.py`: Contact form processing

### Data Validation (app/schemas/)
Pydantic models for request/response validation:
- `user.py`: User data validation
- `product.py`: Product data schemas
- `order.py`: Order processing schemas
- `donation.py`: Donation data validation
- `contact.py`: Contact form validation

## Database Management

### Connecting to Database
```bash
# Connect to database
psql -U postgres -h localhost -d jericho_homestead

# Common psql commands
\l         # List all databases
\dt        # List all tables
\d tablename   # Describe table structure
\q         # Quit psql
```

### Useful Queries
```sql
-- Check recent donations
SELECT * FROM donations ORDER BY created_at DESC LIMIT 5;

-- View product inventory
SELECT * FROM products;

-- Check recent orders
SELECT * FROM orders ORDER BY created_at DESC LIMIT 5;

-- View contact messages
SELECT * FROM contacts ORDER BY created_at DESC;
```

### Migrations
The project uses Alembic for database migrations:
1. Models are defined in SQLAlchemy (app/models/)
2. Migrations are managed in app/migrations/
3. Migration workflow:
   ```bash
   # Generate new migration
   alembic revision --autogenerate -m "Description"

   # Apply migrations
   alembic upgrade head

   # Rollback last migration
   alembic downgrade -1
   ```

## Security Notes
- Database credentials should be stored in environment variables
- User passwords should be hashed before storage
- Regular backups recommended
- Monitor database logs for errors

## Development Guidelines
1. Always create migrations for database changes
2. Test migrations in development before production
3. Use CRUD operations from crud/ directory instead of direct database access
4. Validate data using Pydantic schemas before database operations

## Backup and Restore
```bash
# Backup database
pg_dump -U postgres jericho_homestead > backup.sql

# Restore database
psql -U postgres jericho_homestead < backup.sql
```
