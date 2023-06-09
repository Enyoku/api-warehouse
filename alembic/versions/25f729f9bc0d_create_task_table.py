"""create task table

Revision ID: 25f729f9bc0d
Revises: 512d2a18c951
Create Date: 2023-04-15 20:56:53.131653

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25f729f9bc0d'
down_revision = '512d2a18c951'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Task',
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.Column('manager_id', sa.Integer(), nullable=False),
    sa.Column('storekeeper_id', sa.Integer(), nullable=True),
    sa.Column('order_info_id', sa.Integer(), nullable=False),
    sa.Column('task_status', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['manager_id'], ['Employee.id'], ),
    sa.ForeignKeyConstraint(['order_info_id'], ['OrderInfo.order_id'], ),
    sa.ForeignKeyConstraint(['storekeeper_id'], ['Employee.id'], ),
    sa.PrimaryKeyConstraint('task_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Task')
    # ### end Alembic commands ###
