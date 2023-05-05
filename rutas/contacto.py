from flask import Blueprint, render_template,request
from models.contacto import Contact
from utils.db import db

# define un blueprint llamado contactos que agrupa un conjunto de rutas para manejar los contactos en la aplicación web
contactos=Blueprint("contacto",__name__)

@contactos.route('/')
def index():
    contactos= Contact.query.all()
    return render_template('index.html', contactos=contactos)
#Si se envían datos por el formulario, estos 
# son procesados y guardados como un nuevo objeto 
# Contact en la base de datos utilizando las funciones 
# request.form['fullname'], request.form['email'] 
# y request.form['phone']. 
@contactos.route('/new',methods=['POST'])
def new():
    if request.method=='POST':
        fullname=request.form['fullname']
        email=request.form['email']
        phone=request.form['phone']
        
        new_contact=Contact(fullname,email,phone)
        db.session.add(new_contact)
        #se confirma el cambio con db.session.commit()
        db.session.commit()
    return 'request con datos'