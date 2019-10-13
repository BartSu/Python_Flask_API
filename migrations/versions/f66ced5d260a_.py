"""empty message

Revision ID: f66ced5d260a
Revises: 8ac7cf6732b6
Create Date: 2019-10-13 03:23:34.008886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f66ced5d260a'
down_revision = '8ac7cf6732b6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('postweibos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('weibo_id', sa.String(length=150), nullable=False),
    sa.Column('at_user_id', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('at_user_id'),
    sa.UniqueConstraint('weibo_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('postweibos')
    # ### end Alembic commands ###