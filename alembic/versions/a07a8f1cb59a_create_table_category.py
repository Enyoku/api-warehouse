"""create table category

Revision ID: a07a8f1cb59a
Revises: 325d3c019a2c
Create Date: 2023-04-13 22:58:51.506525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a07a8f1cb59a'
down_revision = '325d3c019a2c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Category',
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('category_id'),
    sa.UniqueConstraint('category_name')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Category')
    # ### end Alembic commands ###