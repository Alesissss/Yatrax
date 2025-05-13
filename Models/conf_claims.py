import bd

class Conf_Claims:
    def __init__(self, id=None, nombre=None, estado=None, idPadre=None):
        self.id = id
        self.nombre = nombre
        self.estado = estado
        self.idPadre = idPadre

    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            menus = conexion.obtener("SELECT id, nombre, estado, idPadre FROM conf_claims WHERE estado = 1")
            return menus
        finally:
            conexion.cerrar()