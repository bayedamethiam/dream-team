"""empty message

Revision ID: e3b8b7681630
Revises: 
Create Date: 2021-01-19 03:09:11.602363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3b8b7681630'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ticket',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_cr', sa.Integer(), nullable=True),
    sa.Column('titre', sa.String(length=60), nullable=True),
    sa.Column('nature', sa.String(length=60), nullable=True),
    sa.Column('categorie', sa.String(length=60), nullable=True),
    sa.Column('sous_categorie', sa.String(length=60), nullable=True),
    sa.Column('equipement', sa.String(length=60), nullable=True),
    sa.Column('adresse', sa.String(length=60), nullable=True),
    sa.Column('site', sa.String(length=60), nullable=True),
    sa.Column('heure_creation', sa.DateTime(), nullable=False),
    sa.Column('heure_arrive', sa.DateTime(), nullable=True),
    sa.Column('heure_retablissement', sa.DateTime(), nullable=True),
    sa.Column('Entrepise', sa.String(length=60), nullable=True),
    sa.Column('Entrepise1', sa.String(length=60), nullable=True),
    sa.Column('Entreprise2', sa.String(length=60), nullable=True),
    sa.Column('duree_demandé', sa.Float(), nullable=True),
    sa.Column('duree_realisé', sa.Float(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('statut', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ticket')
    # ### end Alembic commands ###
