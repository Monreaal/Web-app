from flask import Flask # desde libreria flask importar clase   Flask
from flask_restful import Api, Resource

from rutas import crear_rutas #asi concetamos el appi sin terminar haciendo referencias circulares

# Creamos un objeto de tipo Flask
app = Flask(__name__)

# Creamos un objeto de tipo Api
# Le damos el objeto app

# El parametro/argumento que espera recibir es el objeto de Flask (app)
api = Api(app) # La API sera el programa que se comunique ocn el dispositivo fisico
# La API sera el programa que se comunique con el dispositivo fisico
crear_rutas(api)

# del obejo app ejecutamos el metodo run

app.run(port=5000, debug=True) # http://127.0.0.1: <-- Ip Loop Back / IP Local