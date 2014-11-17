"""empty message

Revision ID: 372f01e16720
Revises: None
Create Date: 2014-11-16 21:18:47.145000

"""

# revision identifiers, used by Alembic.
revision = '372f01e16720'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('f_name', sa.String(length=100), nullable=True),
    sa.Column('l_name', sa.String(length=100), nullable=True),
    sa.Column('full_name', sa.String(length=200), nullable=True),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('profile_url', sa.String(length=1000), nullable=True),
    sa.Column('profile_pic', sa.String(length=1000), nullable=True),
    sa.Column('verified_email', sa.Boolean(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('desc', sa.String(length=1000), nullable=True),
    sa.Column('address_one', sa.String(length=1000), nullable=False),
    sa.Column('address_two', sa.String(length=1000), nullable=True),
    sa.Column('city', sa.String(length=100), nullable=True),
    sa.Column('state', sa.String(length=100), nullable=True),
    sa.Column('country', sa.String(length=100), nullable=True),
    sa.Column('phone_one', sa.String(length=100), nullable=True),
    sa.Column('phone_two', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.Column('url', sa.String(length=1000), nullable=True),
    sa.Column('lon', sa.Float(), nullable=True),
    sa.Column('lat', sa.Float(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('openings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location_id', sa.Integer(), nullable=True),
    sa.Column('day', sa.Integer(), nullable=True),
    sa.Column('open_time_one', sa.Integer(), nullable=True),
    sa.Column('close_time_one', sa.Integer(), nullable=True),
    sa.Column('open_time_two', sa.Integer(), nullable=True),
    sa.Column('close_time_two', sa.Integer(), nullable=True),
    sa.Column('closed', sa.Boolean(), nullable=True),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['location_id'], ['locations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('openings')
    op.drop_table('locations')
    op.drop_table('users')
    ### end Alembic commands ###