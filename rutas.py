# Rutas de acceso a cada recurso de nuestro servidor
from recursos import HolaMundo,PantallaInicio # Tambien se puede importar todo usando *
# Tener el codigo api
def crear_rutas(api):
    # Quiero que puedas acceder a este recurso por medio de tal ruta
    # 1. El recurso que va a ejecutar - Invocar
    # 2. la direccion de este recurso
    api.add_resource(HolaMundo,'/hola')
    api.add_resource(PantallaInicio,'/')     # La ruta de inicio '/'