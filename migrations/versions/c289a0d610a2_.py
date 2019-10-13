"""empty message

Revision ID: c289a0d610a2
Revises: f66ced5d260a
Create Date: 2019-10-13 03:50:37.320954

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c289a0d610a2'
down_revision = 'f66ced5d260a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('postweibos_at_user_id_key', 'postweibos', type_='unique')
    op.drop_constraint('postweibos_weibo_id_key', 'postweibos', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('postweibos_weibo_id_key', 'postweibos', ['weibo_id'])
    op.create_unique_constraint('postweibos_at_user_id_key', 'postweibos', ['at_user_id'])
    # ### end Alembic commands ###