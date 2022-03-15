"""add content to posts table

Revision ID: 0e54a6e2fa0a
Revises: 4deaeb2d22cc
Create Date: 2022-03-11 15:23:25.070859

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e54a6e2fa0a'
down_revision = '4deaeb2d22cc'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
