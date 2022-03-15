"""create post table

Revision ID: 4deaeb2d22cc
Revises: 
Create Date: 2022-03-11 14:52:28.249168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4deaeb2d22cc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column(
        'id', sa.Integer(), nullable=False, primary_key=True), sa.Column(
        'title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
