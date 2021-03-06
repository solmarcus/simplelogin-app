"""empty message

Revision ID: 67c61eead8d2
Revises: 541ce53ab6e9
Create Date: 2020-03-22 23:58:02.672562

"""
import sqlalchemy_utils
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67c61eead8d2'
down_revision = '541ce53ab6e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contact', sa.Column('is_cc', sa.Boolean(), server_default='0', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contact', 'is_cc')
    # ### end Alembic commands ###
