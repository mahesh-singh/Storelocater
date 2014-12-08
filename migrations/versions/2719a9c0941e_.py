"""empty message

Revision ID: 2719a9c0941e
Revises: 2a38643096c0
Create Date: 2014-12-04 17:05:00.972000

"""

# revision identifiers, used by Alembic.
revision = '2719a9c0941e'
down_revision = '2a38643096c0'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('locations', sa.Column('zip_code', sa.String(length=10), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('locations', 'zip_code')
    ### end Alembic commands ###
