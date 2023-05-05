from flask import Blueprint, render_template,request
from models.contacto import Contact
from utils.db import db


contactos=Blueprint("contacto",__name__)

@contactos.route('/')
def index():
    contactos= Contact.query.all()
    return render_template('index.html', contactos=contactos)

@contactos.route('/new',methods=['POST'])
def new():
    if request.method=='POST':
        fullname=request.form['fullname']
        email=request.form['email']
        phone=request.form['phone']
        
        new_contact=Contact(fullname,email,phone)
        db.session.add(new_contact)
        db.session.commit()
    return 'request con datos'