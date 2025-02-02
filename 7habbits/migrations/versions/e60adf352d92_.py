"""empty message

Revision ID: e60adf352d92
Revises: dc7f1400f0f0
Create Date: 2024-12-01 21:11:01.022058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e60adf352d92'
down_revision = 'dc7f1400f0f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('habbit7',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('year', sa.String(length=4), nullable=True),
    sa.Column('week', sa.String(length=8), nullable=True),
    sa.Column('activity', sa.String(length=2000), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('habbit7', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_habbit7_email'), ['email'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('habbit7', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_habbit7_email'))

    op.drop_table('habbit7')
    # ### end Alembic commands ###
