"""empty message

Revision ID: e9cf26489a5a
Revises: 1c6f449849a2
Create Date: 2024-10-30 23:54:32.282355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9cf26489a5a'
down_revision = '1c6f449849a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('answer_no1', sa.Text(), nullable=True),
    sa.Column('answer_no2', sa.Text(), nullable=True),
    sa.Column('answer_no3', sa.Text(), nullable=True),
    sa.Column('answer_no4', sa.Text(), nullable=True),
    sa.Column('answer_no5', sa.Text(), nullable=True),
    sa.Column('answer_no6', sa.Text(), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_answer_email'), ['email'], unique=True)

    op.create_table('position',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('roll', sa.Text(), nullable=True),
    sa.Column('area_avility', sa.Text(), nullable=True),
    sa.Column('area_concern', sa.Text(), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('position', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_position_email'), ['email'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('position', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_position_email'))

    op.drop_table('position')
    with op.batch_alter_table('answer', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_answer_email'))

    op.drop_table('answer')
    # ### end Alembic commands ###
