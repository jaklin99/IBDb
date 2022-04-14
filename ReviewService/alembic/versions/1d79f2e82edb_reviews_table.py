"""reviews_table

Revision ID: 1d79f2e82edb
Revises: 
Create Date: 2022-04-05 18:21:57.783690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d79f2e82edb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'Reviews',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('content', sa.String(length=255), nullable=False),
        sa.Column('date', sa.String(length=255), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('Reviews')
