"""empty message

Revision ID: 197c042172c1
Revises: fdc5c030b1fb
Create Date: 2022-10-13 17:14:42.270267

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '197c042172c1'
down_revision = 'fdc5c030b1fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('des', sa.String(), nullable=True),
    sa.Column('incase', sa.String(), nullable=True),
    sa.Column('image_file', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('des'),
    sa.UniqueConstraint('name')
    )
    op.create_unique_constraint(None, 'course', ['name'])
    op.create_unique_constraint(None, 'course', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'course', type_='unique')
    op.drop_constraint(None, 'course', type_='unique')
    op.drop_table('item')
    # ### end Alembic commands ###
