from flask import Flask
from rutas.contacto import contactos
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI
from utils.db import db
  
#se crea una instancia de Flask llamada "app"
app = Flask(__name__)


print(DATABASE_CONNECTION_URI)
app.config["SQLALCHEMY_DATABASE_URI"]=DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
#se inicializa el objeto SQLAlchemy con la aplicación Flask
db.init_app(app)


#SQLAlchemy(app)
#se registra la ruta "contactos" de la aplicación Flask 
# para que esté disponible en el navegador web y los usuarios 
# puedan realizar operaciones CRUD en la base de datos
app.register_blueprint(contactos)