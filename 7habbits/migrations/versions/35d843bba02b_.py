"""empty message

Revision ID: 35d843bba02b
Revises: ae8053ff8b4f
Create Date: 2024-11-24 15:34:50.431528

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '35d843bba02b'
down_revision = 'ae8053ff8b4f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dailyactivity', schema=None) as batch_op:
        batch_op.alter_column('week',
               existing_type=mysql.VARCHAR(length=7),
               type_=sa.String(length=8),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dailyactivity', schema=None) as batch_op:
        batch_op.alter_column('week',
               existing_type=sa.String(length=8),
               type_=mysql.VARCHAR(length=7),
               existing_nullable=True)

    # ### end Alembic commands ###
