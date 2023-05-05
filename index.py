from app import app
from utils.db import db

#crea un contexto de la aplicación Flask mediante with app.app_context()
with app.app_context():
    db.create_all()
#si el archivo index.py se ejecuta directamente, es decir, 
# no se está importando como un módulo, entonces 
# se ejecuta app.run(debug=True) para iniciar el 
# servidor de desarrollo en el puerto 5000
if __name__ == '__main__':
    app.run(debug=True)