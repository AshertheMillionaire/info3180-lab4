"""empty message

Revision ID: 33eb9b0a9376
Revises: f8b565bc1878
Create Date: 2023-03-08 13:26:51.480039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33eb9b0a9376'
down_revision = 'f8b565bc1878'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=128), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profiles', schema=None) as batch_op:
        batch_op.drop_column('password')

    # ### end Alembic commands ###
