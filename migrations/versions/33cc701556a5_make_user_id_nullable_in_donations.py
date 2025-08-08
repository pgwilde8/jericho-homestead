"""make_user_id_nullable_in_donations

Revision ID: 33cc701556a5
Revises: add_stripe_fields_rev1
Create Date: 2025-08-07 21:52:59.853495

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '33cc701556a5'
down_revision: Union[str, Sequence[str], None] = 'add_stripe_fields_rev1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
