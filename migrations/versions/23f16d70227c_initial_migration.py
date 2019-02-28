"""Initial Migration

Revision ID: 23f16d70227c
Revises: f123b47753f0
Create Date: 2019-02-28 14:36:00.498045

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23f16d70227c'
down_revision = 'f123b47753f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('author', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'author')
    # ### end Alembic commands ###
