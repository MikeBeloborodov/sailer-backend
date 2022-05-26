"""users table

Revision ID: b74be6a654f2
Revises: 21b46ce85994
Create Date: 2022-05-26 20:18:47.719600

"""
from alembic import op
from pyparsing import nullDebugAction
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b74be6a654f2'
down_revision = '21b46ce85994'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                sa.Column('user_id', sa.Integer(), nullable=False, primary_key=True),
                sa.Column('email', sa.String(), nullable=False, unique=True),
                sa.Column('password', sa.String(), nullable=False),
                sa.Column('created_at', sa.TIMESTAMP, nullable=False, server_default=sa.text('now()')),
                sa.Column('updated_at', sa.TIMESTAMP, nullable=False, server_default=sa.text('now()')),
                sa.Column('phone_number', sa.String(), nullable=False, unique=True),
                sa.Column('name', sa.String(), nullable=False,),
                sa.Column('credits', sa.Float(), nullable=False, server_default=sa.text('0')),
                sa.Column('avatar', sa.String(), nullable=True))
    pass


def downgrade():
    pass
