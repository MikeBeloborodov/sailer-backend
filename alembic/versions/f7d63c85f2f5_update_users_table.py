"""update users table

Revision ID: f7d63c85f2f5
Revises: b74be6a654f2
Create Date: 2022-05-26 20:49:42.799901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7d63c85f2f5'
down_revision = 'b74be6a654f2'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column("users", "credits", new_column_name="user_credits")
    pass


def downgrade():
    op.alter_column("users", "user_credits", new_column_name="credits")
    pass
