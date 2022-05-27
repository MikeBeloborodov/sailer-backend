"""change nullable of sold and reserved

Revision ID: 0e0568736fe0
Revises: 73eec441173c
Create Date: 2022-05-27 16:47:40.454418

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e0568736fe0'
down_revision = '73eec441173c'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column("items", "sold", nullable=False, server_default=sa.text('false'))
    op.alter_column("items", "reserved", nullable=False, server_default=sa.text('false'))
    pass


def downgrade():
    op.alter_column("items", "sold", nullable=True)
    op.alter_column("items", "reserved", nullable=True)
    pass
