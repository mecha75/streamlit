"""empty message

Revision ID: ae8053ff8b4f
Revises: e0d9a64995b9
Create Date: 2024-11-24 01:38:34.922685

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ae8053ff8b4f'
down_revision = 'e0d9a64995b9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dailyactivity', schema=None) as batch_op:
        batch_op.alter_column('week',
               existing_type=mysql.VARCHAR(length=2),
               type_=sa.String(length=7),
               existing_nullable=True)

    with op.batch_alter_table('roleweek', schema=None) as batch_op:
        batch_op.alter_column('week',
               existing_type=mysql.VARCHAR(length=2),
               type_=sa.String(length=7),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('roleweek', schema=None) as batch_op:
        batch_op.alter_column('week',
               existing_type=sa.String(length=7),
               type_=mysql.VARCHAR(length=2),
               existing_nullable=True)

    with op.batch_alter_table('dailyactivity', schema=None) as batch_op:
        batch_op.alter_column('week',
               existing_type=sa.String(length=7),
               type_=mysql.VARCHAR(length=2),
               existing_nullable=True)

    # ### end Alembic commands ###