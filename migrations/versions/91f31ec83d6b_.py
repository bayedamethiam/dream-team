"""empty message

Revision ID: 91f31ec83d6b
Revises: e3b8b7681630
Create Date: 2021-01-19 05:30:41.588065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91f31ec83d6b'
down_revision = 'e3b8b7681630'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ticket', sa.Column('la', sa.Float(), nullable=True))
    op.add_column('ticket', sa.Column('lng', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ticket', 'lng')
    op.drop_column('ticket', 'la')
    # ### end Alembic commands ###