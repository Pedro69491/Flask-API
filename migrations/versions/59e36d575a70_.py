"""empty message

Revision ID: 59e36d575a70
Revises: ba406da008a2
Create Date: 2020-07-19 19:37:06.961277

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59e36d575a70'
down_revision = 'ba406da008a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.String(length=80), nullable=True))
    op.create_unique_constraint(None, 'user', ['password'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'password')
    # ### end Alembic commands ###
