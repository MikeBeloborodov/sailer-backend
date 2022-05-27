"""create items table

Revision ID: 19f942975e74
Revises: f7d63c85f2f5
Create Date: 2022-05-27 12:26:30.821170

"""
from tokenize import String
from alembic import op
from pyparsing import col
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19f942975e74'
down_revision = 'f7d63c85f2f5'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('items',
                sa.Column('item_id', sa.Integer(), nullable=False, primary_key=True),
                sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
                sa.Column('updated_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
                sa.Column('owner_id', sa.Integer(), sa.ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False),
                sa.Column('title', sa.String(), nullable=False),
                sa.Column('description', sa.String(), nullable=False),
                sa.Column('cathegory', sa.String(), nullable=False),
                sa.Column('address', sa.String(), nullable=False),
                sa.Column('condition', sa.String(), nullable=False),
                sa.Column('price', sa.Float(), nullable=False),
                sa.Column('photo', sa.String(), nullable=True),
                sa.Column('buyer_id', sa.Integer(), sa.ForeignKey("users.user_id", ondelete="CASCADE"), nullable=True),
                sa.Column('transaction_id', sa.Integer(), nullable=True),
                sa.Column('sold_at', sa.TIMESTAMP(timezone=True), nullable=True),
                sa.Column('reserved', sa.Boolean(), nullable=True, server_default=sa.text('false')),
                sa.Column('sold', sa.Boolean(), nullable=True, server_default=sa.text('false')))
    pass

def downgrade():
    op.drop_table('items')
    pass
