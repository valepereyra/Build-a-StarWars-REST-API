"""empty message

Revision ID: c535ef9350d7
Revises: e1416f8a79c4
Create Date: 2023-01-26 14:40:07.115747

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c535ef9350d7'
down_revision = 'e1416f8a79c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favoritos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('agregar', sa.String(length=250), nullable=False),
    sa.Column('eliminar', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favoritos')
    # ### end Alembic commands ###
