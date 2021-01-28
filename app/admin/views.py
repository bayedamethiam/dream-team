# app/admin/views.py
import googlemaps
import os, sys, subprocess, platform
from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from datetime import date,datetime
from . import admin
from .forms import DepartmentForm, RoleForm, EmployeeAssignForm,ticketForm,etatForm
from .. import db
from ..models import Department, Role, Employee
from ..models import Cil,Ticket,Cr,Equipement
import folium
import smtplib
from sqlalchemy import func
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import make_response


import pdfkit
from flask import request
# app/admin/views.py

# update imports

# app/admin/views.py





# Role Views


def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)


# Department Views


@admin.route('/departments', methods=['GET', 'POST'])
@login_required
def list_departments():
    """
    List all departments
    """
    check_admin()

    departments = Department.query.all()

    return render_template('admin/departments/departments.html',
                           departments=departments, title="Departments")


@admin.route('/departments/add', methods=['GET', 'POST'])
@login_required
def add_department():
    """
    Add a department to the database
    """
    check_admin()

    add_department = True

    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(name=form.name.data,
                                description=form.description.data)
        try:
            # add department to the database
            db.session.add(department)
            db.session.commit()
            flash('You have successfully added a new department.')
        except:
            # in case department name already exists
            flash('Error: department name already exists.')

        # redirect to departments page
        return redirect(url_for('admin.list_departments'))

    # load department template
    return render_template('admin/departments/department.html', action="Add",
                           add_department=add_department, form=form,
                           title="Add Department")


@admin.route('/departments/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_department(id):
    """
    Edit a department
    """
    check_admin()

    add_department = False

    department = Department.query.get_or_404(id)
    form = DepartmentForm(obj=department)
    if form.validate_on_submit():
        department.name = form.name.data
        department.description = form.description.data
        db.session.commit()
        flash('You have successfully edited the department.')

        # redirect to the departments page
        return redirect(url_for('admin.list_departments'))

    form.description.data = department.description
    form.name.data = department.name
    return render_template('admin/departments/department.html', action="Edit",
                           add_department=add_department, form=form,
                           department=department, title="Edit Department")


@admin.route('/departments/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_department(id):
    """
    Delete a department from the database
    """
    check_admin()

    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    flash('You have successfully deleted the department.')

    # redirect to the departments page
    return redirect(url_for('admin.list_departments'))

    return render_template(title="Delete Department")


@admin.route('/roles')
@login_required
def list_roles():
    check_admin()
    """
    List all roles
    """
    roles = Role.query.all()
    return render_template('admin/roles/roles.html',
                           roles=roles, title='Roles')


@admin.route('/roles/add', methods=['GET', 'POST'])
@login_required
def add_role():
    """
    Add a role to the database
    """
    check_admin()

    add_role = True

    form = RoleForm()
    if form.validate_on_submit():
        role = Role(name=form.name.data,
                    description=form.description.data)

        try:
            # add role to the database
            db.session.add(role)
            db.session.commit()
            flash('You have successfully added a new role.')
        except:
            # in case role name already exists
            flash('Error: role name already exists.')

        # redirect to the roles page
        return redirect(url_for('admin.list_roles'))

    # load role template
    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title='Add Role')


@admin.route('/roles/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_role(id):
    """
    Edit a role
    """
    check_admin()

    add_role = False

    role = Role.query.get_or_404(id)
    form = RoleForm(obj=role)
    if form.validate_on_submit():
        role.name = form.name.data
        role.description = form.description.data
        db.session.add(role)
        db.session.commit()
        flash('You have successfully edited the role.')

        # redirect to the roles page
        return redirect(url_for('admin.list_roles'))

    form.description.data = role.description
    form.name.data = role.name
    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title="Edit Role")


@admin.route('/roles/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_role(id):
    """
    Delete a role from the database
    """
    check_admin()

    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()
    flash('You have successfully deleted the role.')

    # redirect to the roles page
    return redirect(url_for('admin.list_roles'))

    return render_template(title="Delete Role")


@admin.route('/employees')
@login_required
def list_employees():
    """
    List all employees
    """
    check_admin()

    employees = Employee.query.all()
    return render_template('admin/employees/employees.html',
                           employees=employees, title='Employees')


@admin.route('/employees/assign/<int:id>', methods=['GET', 'POST'])
@login_required
def assign_employee(id):
    """
    Assign a department and a role to an employee
    """
    check_admin()

    employee = Employee.query.get_or_404(id)

    # prevent admin from being assigned a department or role
    if employee.is_admin:
        abort(403)

    form = EmployeeAssignForm(obj=employee)
    if form.validate_on_submit():
        employee.department = form.department.data
        employee.role = form.role.data
        db.session.add(employee)
        db.session.commit()
        flash('You have successfully assigned a department and role.')

        # redirect to the roles page
        return redirect(url_for('admin.list_employees'))

    return render_template('admin/employees/employee.html',
                           employee=employee, form=form,
                           title='Assign Employee')









@admin.route('/tickets', methods=['GET', 'POST'])
@login_required
def list_tickets():
   
    
    

   
    tickets = Ticket.query.all()

    nb_ticket=db.session.query(func.count(Ticket.id)).all()
    nb_ticket=str(nb_ticket[0]).replace("(","").replace(")","").replace(",","")

    nb_ticket_cours=db.session.query(func.count(Ticket.id)).filter(Ticket.statut.like("Intervention en cours")).all()
    nb_ticket_cours=str(nb_ticket_cours[0]).replace("(","").replace(")","").replace(",","")
  
    nb_ticket_gelé=db.session.query(func.count(Ticket.id)).filter(Ticket.statut.like("Gelé")).all()
    nb_ticket_gelé=str(nb_ticket_gelé[0]).replace("(","").replace(")","").replace(",","")
  
    nb_ticket_terminé=db.session.query(func.count(Ticket.id)).filter(Ticket.statut.like("Terminé")).all()
    nb_ticket_terminé=str(nb_ticket_terminé[0]).replace("(","").replace(")","").replace(",","")
  

    return render_template('admin/tickets.html',tickets=tickets, title="Tickets" , nom=current_user.last_name,nb_ticket=nb_ticket,nb_ticket_cours=nb_ticket_cours,nb_ticket_gelé=nb_ticket_gelé,nb_ticket_terminé=nb_ticket_terminé)


@admin.route('/tickets/admin', methods=['GET', 'POST'])
@login_required
def list_tickets_etat():
    """
    List all tickets
    """
    check_admin()
    

    tickets = Ticket.query.all()

    return render_template('admin/tickets/tickets_statut.html',
                           tickets=tickets, title="Tickets" , nom=current_user.last_name)


@admin.route('/tickets/add', methods=['GET', 'POST'])
@login_required
def add_ticket():
    """
    Add a ticket to the database
    """
    

    add_ticket = True
    
    form = ticketForm()
    if form.validate_on_submit():

        gmaps_key = googlemaps.Client(key = "AIzaSyBPSB9oo1RWjfB20Zv2qTe7-lRMcw7ocfM")

        geocode_result=gmaps_key.geocode(form.adresse.data)
        try:
            lat=geocode_result[0]["geometry"]["location"]["lat"]
            lon=geocode_result[0]["geometry"]["location"]["lng"]
            ticket = Ticket(titre=form.titre.data,
                            nature=form.nature.data,
                            categorie=form.categorie.data,
                            sous_categorie=form.sous_categorie.data,
                            equipement=form.equipement.data,
                            adresse=form.adresse.data,
                            site=form.site.data,
                            description=form.description.data,
                            lng=lon,
                            la=lat
                            )
        except:
            flash('veuillez verifier votre adresse')
            return render_template('admin/ticket.html', action="Add",
                           add_ticket=add_ticket, form=form,
                           title="Creer ticket" )
            lat = None
            lon = None

        try:
            # add ticket to the database
            db.session.add(ticket)
            db.session.commit()
            flash('You have successfully added a new ticket.')
        except:
            # in case ticket name already exists
            flash('Error: ticket name already exists.')

        # redirect to tickets page
        return redirect(url_for('admin.list_tickets'))

    # load ticket template
    return render_template('admin/ticket.html', action="Add",
                           add_ticket=add_ticket, form=form,
                           title="Creer ticket" )


@admin.route('/tickets/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_ticket(id):
    """
    Edit a  ticket
    """
    

    add_ticket = False

    ticket = Ticket.query.get_or_404(id)
    form = ticketForm(obj=ticket)
    if form.validate_on_submit():



        ticket.titre=form.titre.data
        ticket.nature=form.description.data
        ticket.categorie=form.description.data
        ticket.sous_categorie=form.description.data
        ticket.equipement=form.description.data
        ticket.adresse=form.description.data
        ticket.site=form.description.data
        ticket.description=form.description.data
                                

        db.session.commit()
        flash('You have successfully edited the Ticket.')

        # redirect to the tickets page
        return redirect(url_for('admin.list_tickets'))

    ticket.titre=form.titre.data
    ticket.nature=form.description.data
    ticket.categorie=form.description.data
    ticket.sous_categorie=form.description.data
    ticket.equipement=form.description.data
    ticket.adresse=form.description.data
    ticket.site=form.description.data
    ticket.description=form.description.data
    return render_template('admin/ticket.html', action="Edit",
                           add_ticket=add_ticket, form=form,
                           ticket=ticket, title="Modifier un ticket")




@admin.route('/tickets/etat/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_etat(id):
    """
    Edit a  ticket
    """
    """
    Edit a  ticket
    """
    check_admin()

    add_ticket = False

    ticket = Ticket.query.get_or_404(id)
    form = etatForm(obj=ticket)
    if form.validate_on_submit():


        msg = MIMEMultipart()
        msg['From'] = 'pinguard.2021@gmail.com'
        msg['To'] = 'bayedame16@gmail.com'
        msg['Subject'] = 'Etat Ticket' 
        




        prev=ticket.statut
        ticket.statut=form.statut.data
            
        if form.statut.data == 'Intervention en cours':
            ticket.heure_arrive = datetime.utcnow()
            message = 'Bonjour ! nos techniciens sont arrivé sur site pour effectuer l intervention a '+str(datetime.utcnow())
            msg.attach(MIMEText(message))
            mailserver = smtplib.SMTP('smtp.gmail.com', 587)
            mailserver.ehlo()
            mailserver.starttls()
            mailserver.ehlo()
            mailserver.login('pinguard.2021@gmail.com', 'Pinguard2021')
            mailserver.sendmail('pinguard.2021@gmail.com', form.email.data, msg.as_string())
            mailserver.quit()






        if form.statut.data == 'Gelé':

            
            ticket.heure_gele = datetime.utcnow()

            message = 'Bonjour ! le ticket a ete gelé  '+str(datetime.utcnow())
            msg.attach(MIMEText(message))
            mailserver = smtplib.SMTP('smtp.gmail.com', 587)
            mailserver.ehlo()
            mailserver.starttls()
            mailserver.ehlo()
            mailserver.login('pinguard.2021@gmail.com', 'Pinguard2021')
            mailserver.sendmail('pinguard.2021@gmail.com', form.email.data, msg.as_string())
            mailserver.quit()



        if (prev == 'Gelé') & (form.statut.data == 'Intervention en cours'):

            ticket.heure_degele=datetime.utcnow()
            message = 'Bonjour ! le ticket a ete degelé  '+str(datetime.utcnow())
            msg.attach(MIMEText(message))
            mailserver = smtplib.SMTP('smtp.gmail.com', 587)
            mailserver.ehlo()
            mailserver.starttls()
            mailserver.ehlo()
            mailserver.login('pinguard.2021@gmail.com', 'Pinguard2021')
            mailserver.sendmail('pinguard.2021@gmail.com', form.email.data, msg.as_string())
            mailserver.quit()




        if form.statut.data == 'Terminé':
          
            ticket.heure_retablissement = datetime.utcnow()
            message = 'Bonjour ! l intervention est terminé veuillez consulter le compte rendu et le valider  '+str(datetime.utcnow())
            msg.attach(MIMEText(message))
            mailserver = smtplib.SMTP('smtp.gmail.com', 587)
            mailserver.ehlo()
            mailserver.starttls()
            mailserver.ehlo()
            mailserver.login('pinguard.2021@gmail.com', 'Pinguard2021')
            mailserver.sendmail('pinguard.2021@gmail.com', form.email.data, msg.as_string())
            mailserver.quit()



        if form.statut.data == 'Validé':
            ticket.heure_validation = datetime.utcnow()
            message = 'Bonjour ! vous avez validé le compte rendu et notre intervention merci !  '+str(datetime.utcnow())
            msg.attach(MIMEText(message))
            mailserver = smtplib.SMTP('smtp.gmail.com', 587)
            mailserver.ehlo()
            mailserver.starttls()
            mailserver.ehlo()
            mailserver.login('pinguard.2021@gmail.com', 'Pinguard2021')
            mailserver.sendmail('pinguard.2021@gmail.com', form.email.data, msg.as_string())
            mailserver.quit()
                                

        db.session.commit()
        flash('You have successfully edited the Ticket.')

        # redirect to the tickets page
        return redirect(url_for('admin.list_tickets_etat'))

    
    ticket.statut=form.statut.data
    return render_template('admin/tickets/ticket_statut.html', action="Edit",form=form,ticket=ticket, title="Modifier un ticket")





















@admin.route('/tickets/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_ticket(id):
    """
    Delete a ticket from the database
    """
    check_admin()

    ticket = Ticket.query.get_or_404(id)
    db.session.delete(ticket)
    db.session.commit()
    flash('You have successfully deleted the ticket.')

    # redirect to the tickets page
    return redirect(url_for('admin.list_tickets'))

    return render_template(title="Delete ticket")



@admin.route('/map/', methods=['GET', 'POST'])
@login_required
def map_ticket():

    cils = Cil.query.all()
    tickets = Ticket.query.all()

    m = folium.Map(location=[46.795135, 2.587876],  zoom_start=6.4)

    #position des CIL

    for cil in cils :
        if cil.entreprise == "Pinguard":

            folium.Marker(
                location=[cil.lat,cil.longi],
                popup="<i>"+cil.nom+" "+ "Techniciens :"+str(cil.nb_technicien)+"</i>",
                tooltip="CIL",
                icon=folium.Icon(prefix='fa', icon='exclamation',color='blue')
            ).add_to(m)

        else :

            if cil.entreprise == "ProBTP":
                folium.Marker(
                    location=[cil.lat,cil.longi],
                    popup="<i>"+cil.nom+" "+ "Techniciens :"+str(cil.nb_technicien)+"</i>",
                    tooltip="CIL",
                    icon=folium.Icon(prefix='fa', icon='exclamation',color='purple')
                ).add_to(m)

            else :
                folium.Marker(
                    location=[cil.lat,cil.longi],
                    popup="<i>"+cil.nom+" "+ "Techniciens :"+str(cil.nb_technicien)+"</i>",
                    tooltip="CIL",
                    icon=folium.Icon(prefix='fa', icon='exclamation',color='darkblue')
                ).add_to(m)

        

    #position des intervention
    for ticket in tickets:

        if ticket.statut == "Non traité":


            folium.Marker(
                    location=[ticket.la,ticket.lng],
                    popup="<i>Pas encore pris en charge </i>",
                    tooltip="Intervention",
                    icon=folium.Icon(color='red')
                ).add_to(m)

        else:

            if ticket.statut == "Gelé":
                olium.Marker(
                    location=[ticket.la,ticket.lng],
                    popup="<i>Ticket gelé </i>",
                    tooltip="Click here",
                    icon=folium.Icon(prefix='fa', icon='exclamation',color='black')
                    ).add_to(m)

            else:

                if  ticket.statut == "Intervention en cours":
                        
                    folium.Marker(
                        location=[ticket.la,ticket.lng],
                        popup="<i>Intervention en cours </i>",
                        tooltip="Click here",
                        icon=folium.Icon(prefix='fa', icon='exclamation',color='orange')
                        ).add_to(m)

                else:

                    if ticket.statut == "Pris en charge":

                        folium.Marker(
                            location=[ticket.la,ticket.lng],
                            popup="<i>Technicien en route</i>",
                            tooltip="Click here",
                            icon=folium.Icon(prefix='fa', icon='exclamation',color='lightred')
                            ).add_to(m)

                    else:

                        if ticket.statut == "Terminé":
                            folium.Marker(
                                location=[ticket.la,ticket.lng],
                                popup="<i>Intervention en cours </i>",
                                tooltip="Click here",
                                icon=folium.Icon(prefix='fa', icon='exclamation',color='green')
                                ).add_to(m)





            
            


    return render_template('admin/map.html', m=m._repr_html_())




@admin.route('/etat/', methods=['GET', 'POST'])
@login_required
def change_etat():


   
    return render_template('basee.html')





@admin.route('/test/', methods=['GET', 'POST'])
@login_required
def cil_test():

    tickets = Ticket.query.all()
   
    return render_template('admin/cr.html')


@admin.route('test//test/', methods=['GET', 'POST'])
def test():


   
    return "hello world"





@admin.route('/cr/<int:id>', methods=['GET', 'POST'])
@login_required
def cr_test(id):

  
    ticket = Ticket.query.get_or_404(id)
    if request.method == 'POST':

        m = folium.Map(location=[46.795135, 2.587876],  zoom_start=6.4)
        folium.Marker(
                location=[ticket.la,ticket.lng],
                popup=ticket.statut,
                tooltip="Intervention",
                icon=folium.Icon(color='red')
            ).add_to(m)


        nom1=request.form.get('Nom1')
        specialisation1=request.form.get('Specialisation1')
        nb_intervention1=request.form.get('nb_intervention1')
        entreprise1=request.form.get('entreprise1')
        telephone1=request.form.get('telephone1')
        mail1=request.form.get('mail1')


        nom2=request.form.get('Nom2')
        specialisation2=request.form.get('Specialisation2')
        nb_intervention2=request.form.get('nb_intervention2')
        entreprise2=request.form.get('entreprise2')
        telephone2=request.form.get('telephone2')
        mail2=request.form.get('mail2')

        nom3=request.form.get('Nom3')
        specialisation3=request.form.get('Specialisation3')
        nb_intervention3=request.form.get('nb_intervention3')
        entreprise3=request.form.get('entreprise3')
        telephone3=request.form.get('telephone3')
        mail3=request.form.get('mail3')


        techno=request.form.get('techno')
        constructeur=request.form.get('constructeur')
        equipement=request.form.get('equipement')
        raison=request.form.get('raison')
        solution=request.form.get('solution')
        nature=request.form.get('nature')
        
        
        

       
        flash('You have successfully edited the Ticket.')

        # redirect to the tickets page
        html = render_template('admin/cr.html',m=m._repr_html_(),nb_intervention3=nb_intervention3,nb_intervention1=nb_intervention1,nb_intervention2=nb_intervention2, nature=nature, telephone1=telephone1, telephone2=telephone2, telephone3=telephone3,  t0=ticket.heure_creation.time(),ticket=ticket,nom1=nom1,specialisation1=specialisation1,entreprise1=entreprise1,mail1=mail1,nom2=nom2,specialisation2=specialisation2,entreprise2=entreprise2,mail2=mail2,nom3=nom3,specialisation3=specialisation3,entreprise3=entreprise3,mail3=mail3,techno=techno,constructeur=constructeur,equipement=equipement,raison=raison,solution=solution)
        
        
      
        pdfkit_config=None
        if platform.system() == "Windows":
                pdfkit_config = pdfkit.configuration(wkhtmltopdf=os.environ.get('WKHTMLTOPDF_BINARY', 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'))
        else:
                os.environ['PATH'] += os.pathsep + os.path.dirname(sys.executable) 
                WKHTMLTOPDF_CMD = subprocess.Popen(['which', os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf')], 
                    stdout=subprocess.PIPE).communicate()[0].strip()
                pdfkit_config = pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_CMD)
        

        pdf=pdfkit.from_string(html,False,configuration=pdfkit_config)
        pdf = pdfkit.from_string(html, False,configuration=pdfkit_config)
        response = make_response(pdf)
        response.headers["Content-Type"] = "cr/pdf"

        response.headers["Content-Disposition"] = "inline; filename=ticke.pdf"
        return response
        



    #pdfkit.from_url('http://127.0.0.1:5000/admin/cr/','cr.pdf')

    return render_template('admin/redaction_cr.html',  t0=ticket.heure_creation.time(),ticket=ticket)


            


        
            
        

            



        
            
        
