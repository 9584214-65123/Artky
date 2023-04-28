"""empty message

Revision ID: fa451926416f
Revises: 1e5a50177c1b
Create Date: 2022-05-17 17:12:53.471799

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa451926416f'
down_revision = '1e5a50177c1b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('registros', sa.Column('contrasena', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('registros', 'contrasena')
    # ### end Alembic commands ###