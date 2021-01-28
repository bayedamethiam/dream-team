# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField
from wtforms.validators import DataRequired

from wtforms.ext.sqlalchemy.fields import QuerySelectField

from ..models import Department, Role

from ..models import Cil,Ticket,Cr,Equipement


class ticketForm(FlaskForm):
    """
    Form for admin to add or edit a ticket
    """
    
    titre = StringField('titre', validators=[DataRequired()])
    nature = StringField('nature', validators=[DataRequired()])
    categorie = StringField('categorie', validators=[DataRequired()])
    sous_categorie = StringField('sous_categorie')
    equipement = StringField('equipement', validators=[DataRequired()])
    adresse = StringField('adresse', validators=[DataRequired()])
    site = StringField('site', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class etatForm(FlaskForm):
    statut=SelectField('statut', choices=['Non traité','Pris en charge','Intervention en cours','Gelé','Terminé','Validé'])
    email=StringField('email', validators=[DataRequired()])
    submit = SubmitField('Submit')


class DepartmentForm(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')


# app/admin/forms.py

# existing code remains

class RoleForm(FlaskForm):
    """
    Form for admin to add or edit a role
    """
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')



# app/admin/forms.py

# update imports


# existing code remains

class EmployeeAssignForm(FlaskForm):
    """
    Form for admin to assign departments and roles to employees
    """
    department = QuerySelectField(query_factory=lambda: Department.query.all(),
                                  get_label="name")
    role = QuerySelectField(query_factory=lambda: Role.query.all(),
                            get_label="name")
    submit = SubmitField('Submit')

