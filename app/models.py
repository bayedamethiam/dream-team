# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date,datetime
from app import db, login_manager


class Employee(UserMixin, db.Model):
    """
    Create an Employee table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Employee: {}>'.format(self.username)


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Employee.query.get(int(user_id))


class Department(db.Model):
    """
    Create a Department table
    """

    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='department',
                                lazy='dynamic')

    def __repr__(self):
        return '<Department: {}>'.format(self.name)


class Role(db.Model):
    """
    Create a Role table
    """

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('Employee', backref='role',
                                lazy='dynamic')

    def __repr__(self):
        return '<Role: {}>'.format(self.name)


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_cr = db.Column(db.Integer)
    titre = db.Column(db.String(60))
    nature = db.Column(db.String(60))
    categorie = db.Column(db.String(60))
    sous_categorie = db.Column(db.String(60))
    equipement = db.Column(db.String(60))
    adresse = db.Column(db.String(60))
    lng=db.Column(db.Float)
    la=db.Column(db.Float)
    site = db.Column(db.String(60))
    heure_creation = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    heure_arrive = db.Column(db.DateTime)
    heure_gele = db.Column(db.DateTime)
    heure_degele = db.Column(db.DateTime)
    heure_retablissement = db.Column(db.DateTime)
    heure_validation = db.Column(db.DateTime)
    Entrepise = db.Column(db.String(60))
    Entrepise1 = db.Column(db.String(60))
    Entreprise2 = db.Column(db.String(60))
    duree_demandé = db.Column(db.Float)
    duree_realisé= db.Column(db.Float)
    description = db.Column(db.Text)
    statut = db.Column(db.String(60),default="Non traité")

class Cr(db.Model):
    id_cr = db.Column(db.Integer, primary_key=True)
    lien = db.Column(db.Text)

class Cil(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(60))
    nb_technicien = db.Column(db.Integer)
    ville = db.Column(db.String(60))
    entreprise = db.Column(db.String(60))
    adresse = db.Column(db.String(260))
    longi = db.Column(db.Float)
    lat = db.Column(db.Float)


class Equipement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(60))
    cil_id = db.Column(db.Integer,db.ForeignKey('cil.id'))
    quantite = db.Column(db.Float)
    unité = db.Column(db.String(60))