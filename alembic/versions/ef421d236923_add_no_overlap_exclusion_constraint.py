"""add no-overlap exclusion constraint

Revision ID: ef421d236923
Revises: fca9fb20aab6
Create Date: 2026-08-18 19:46:07.454139

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'ef421d236923'
down_revision: Union[str, Sequence[str], None] = 'fca9fb20aab6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.execute("CREATE EXTENSION IF NOT EXISTS btree_gist")
    op.execute(
        """
        ALTER TABLE reservation
        ADD CONSTRAINT no_overlapping_reservations
        EXCLUDE USING gist (
            room_id WITH =,
            tstzrange(start_time, end_time, '[)') WITH &&
        )
        """
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.execute("ALTER TABLE reservation DROP CONSTRAINT no_overlapping_reservations")
    op.execute("DROP EXTENSION IF EXISTS btree_gist")