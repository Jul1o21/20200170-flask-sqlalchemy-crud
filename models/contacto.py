from utils.db import db
#CLASE PARA EL USO DE LOS OBJETOS CONTACTOS OBTENIDOS DE LA BD
class Contact(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    fullname=db.Column(db.String(100))
    email=db.Column(db.String(100))
    phone=db.Column(db.String(100))
    
    def __init__(self,fullname,email,phone ):
        self.fullname=fullname
        self.email   =email
        self.phone   =phone