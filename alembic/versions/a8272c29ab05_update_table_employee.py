"""update table employee

Revision ID: a8272c29ab05
Revises: 3a06d5b80cda
Create Date: 2023-04-11 23:07:46.445450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8272c29ab05'
down_revision = '3a06d5b80cda'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Employee', sa.Column('id', sa.Integer(), nullable=False))
    op.drop_column('Employee', 'employee_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Employee', sa.Column('employee_id', sa.INTEGER(), server_default=sa.text('nextval(\'"Employee_employee_id_seq"\'::regclass)'), autoincrement=True, nullable=False))
    op.drop_column('Employee', 'id')
    # ### end Alembic commands ###
