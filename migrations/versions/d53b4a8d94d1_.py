"""empty message

Revision ID: d53b4a8d94d1
Revises: 769dd873dff8
Create Date: 2022-05-16 22:45:54.344406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd53b4a8d94d1'
down_revision = '769dd873dff8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('catalogos', sa.Column('list_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'catalogos', 'categorias', ['list_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'catalogos', type_='foreignkey')
    op.drop_column('catalogos', 'list_id')
    # ### end Alembic commands ###