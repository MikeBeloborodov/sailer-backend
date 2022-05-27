"""add deleted to items

Revision ID: 73eec441173c
Revises: 2d2425e0b2f2
Create Date: 2022-05-27 16:44:12.648976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73eec441173c'
down_revision = '2d2425e0b2f2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("items", sa.Column("deleted", sa.Boolean(), nullable=False, server_default=sa.text('false')))
    pass


def downgrade():
    op.drop_column("items", "deleted")
    pass
