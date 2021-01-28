import click
from flask.cli import with_appcontext

from .extensions import db

from ..models import Department, Role, Employee
from ..models import Cil,Ticket,Cr,Equipement
@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()