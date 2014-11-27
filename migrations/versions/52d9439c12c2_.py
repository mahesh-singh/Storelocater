"""empty message

Revision ID: 52d9439c12c2
Revises: 372f01e16720
Create Date: 2014-11-23 08:38:19.278000

"""

# revision identifiers, used by Alembic.
revision = '52d9439c12c2'
down_revision = '372f01e16720'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('locations', sa.Column('code', sa.String(length=50), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('locations', 'code')
    ### end Alembic commands ###
