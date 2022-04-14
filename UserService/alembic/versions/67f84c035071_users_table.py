"""users_table

Revision ID: 67f84c035071
Revises: 
Create Date: 2022-04-05 18:04:58.151886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67f84c035071'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'Users',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('username', sa.String(length=255), nullable=False),
<<<<<<< HEAD
        sa.Column('password', sa.String(length=255), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
=======
>>>>>>> 65c530dc3ff53bccb3ee14a8f4b31d4238c52a47
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('Users')
