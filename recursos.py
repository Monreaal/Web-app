from flask_restful import Resource

from flask import make_response, render_template
# Recursos que nuestro servidor tendra disponible


# Vamos a crear recursos - Para poder crear recursos lo hacemos a traves de clases y objetos
class HolaMundo(Resource):
# Los recursos van a poder ejecutar dos acciones -> metodos (GET y POST)
    def get(self):
        return {'Hola': 'Mundo'}

class PantallaInicio(Resource):
    def get(self):
        #renderizamos el contenido html
        contenido = render_template('index.html')

        # Retornamos el contenido renderizado en una respuesta HTTP
        return make_response(contenido)