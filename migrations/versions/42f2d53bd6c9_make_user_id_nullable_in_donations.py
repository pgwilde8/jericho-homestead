"""make_user_id_nullable_in_donations

Revision ID: 42f2d53bd6c9
Revises: 33cc701556a5
Create Date: 2025-08-07 21:53:07.952010

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '42f2d53bd6c9'
down_revision: Union[str, Sequence[str], None] = '33cc701556a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Make user_id nullable in donations table to allow guest donations
    op.alter_column('donations', 'user_id', nullable=True)


def downgrade() -> None:
    """Downgrade schema."""
    # Revert user_id to non-nullable (this might fail if there are NULL values)
    op.alter_column('donations', 'user_id', nullable=False)
