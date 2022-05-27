"""change description

Revision ID: 2d2425e0b2f2
Revises: 19f942975e74
Create Date: 2022-05-27 15:53:39.817254

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d2425e0b2f2'
down_revision = '19f942975e74'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column("items", "description", nullable=True)
    pass


def downgrade():
    op.alter_column("items", "description", nullable=False)
    pass
