"""empty message

Revision ID: 8d418a5040c6
Revises: 5e0bdf3f3cd0
Create Date: 2020-07-22 19:17:10.940041

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d418a5040c6'
down_revision = '5e0bdf3f3cd0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key'),
    sa.UniqueConstraint('password', name='user_password_key'),
    sa.UniqueConstraint('username', name='user_username_key')
    )
    # ### end Alembic commands ###
