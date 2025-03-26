"""init_revision

Revision ID: 6f7e7ca7e9cc
Revises: 
Create Date: 2025-03-22 20:31:06.367788

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '6f7e7ca7e9cc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('wallets',
                    sa.Column('balance', sa.Numeric(), server_default='0.0',
                              nullable=False),
                    sa.Column('id', sa.UUID(), nullable=False),
                    sa.Column('created_at', sa.DateTime(),
                              server_default=sa.text('now()'), nullable=False),
                    sa.Column('updated_at', sa.DateTime(),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('wallets')
