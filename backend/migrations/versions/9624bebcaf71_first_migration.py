"""first migration

Revision ID: 9624bebcaf71
Revises: 
Create Date: 2023-09-06 15:51:42.864268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9624bebcaf71'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tbl_auto_perceived_gender',
    sa.Column('ccn_auto_perceived_gender', sa.Integer(), nullable=False),
    sa.Column('auto_perceived_gender', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('ccn_auto_perceived_gender')
    )
    op.create_table('tbl_type_id',
    sa.Column('ccn_type_id', sa.Integer(), nullable=False),
    sa.Column('type_id', sa.String(length=3), nullable=False),
    sa.Column('description_type_id', sa.String(length=40), nullable=False),
    sa.PrimaryKeyConstraint('ccn_type_id')
    )
    op.create_table('tbl_customer',
    sa.Column('ccn_customer', sa.Integer(), nullable=False),
    sa.Column('ccn_type_id', sa.Integer(), nullable=True),
    sa.Column('number_id_customer', sa.BigInteger(), nullable=False),
    sa.Column('first_name_customer', sa.String(length=60), nullable=False),
    sa.Column('middle_name_customer', sa.String(length=60), nullable=True),
    sa.Column('first_last_name_customer', sa.String(length=60), nullable=False),
    sa.Column('second_last_name_customer', sa.String(length=60), nullable=True),
    sa.Column('birthday_customer', sa.Date(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('auto_perceived_gender', sa.Integer(), nullable=True),
    sa.Column('email_customer', sa.String(length=100), nullable=False),
    sa.Column('cellphone_customer', sa.BigInteger(), nullable=False),
    sa.Column('informed_consent_law_1581', sa.String(length=10), nullable=False),
    sa.Column('profile_picture_customer', sa.String(length=255), nullable=True),
    sa.Column('password_customer', sa.String(length=300), nullable=False),
    sa.ForeignKeyConstraint(['auto_perceived_gender'], ['tbl_auto_perceived_gender.ccn_auto_perceived_gender'], ),
    sa.ForeignKeyConstraint(['ccn_type_id'], ['tbl_type_id.ccn_type_id'], ),
    sa.PrimaryKeyConstraint('ccn_customer'),
    sa.UniqueConstraint('number_id_customer')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tbl_customer')
    op.drop_table('tbl_type_id')
    op.drop_table('tbl_auto_perceived_gender')
    # ### end Alembic commands ###