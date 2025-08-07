"""create shop tables

Revision ID: create_shop_tables
Revises: 1cafc4a0d3df
Create Date: 2024-03-19

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from datetime import datetime

# revision identifiers, used by Alembic.
revision = 'create_shop_tables_rev1'
down_revision = '1cafc4a0d3df'
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Create products table
    op.create_table(
        'products',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('price', sa.Float(), nullable=False),
        sa.Column('image_url', sa.String(255), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.text('now()')),
        sa.PrimaryKeyConstraint('id'),
        sa.Index('ix_products_id', 'id')
    )

    # Create orders table
    op.create_table(
        'orders',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('total_amount', sa.Float(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.text('now()')),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.Index('ix_orders_id', 'id')
    )

    # Create donations table
    op.create_table(
        'donations',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('amount', sa.Float(), nullable=False),
        sa.Column('message', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.text('now()')),
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.Index('ix_donations_id', 'id')
    )

    # Create contacts table
    op.create_table(
        'contacts',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('email', sa.String(100), nullable=False),
        sa.Column('message', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.text('now()')),
        sa.PrimaryKeyConstraint('id'),
        sa.Index('ix_contacts_id', 'id')
    )

def downgrade() -> None:
    op.drop_table('contacts')
    op.drop_table('donations')
    op.drop_table('orders')
    op.drop_table('products') 