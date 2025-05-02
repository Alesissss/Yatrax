import bd

class Conf_Menus:
    def __init__(self, id=None, nombre=None, estado=None, idPadre=None):
        self.id = id
        self.nombre = nombre
        self.estado = estado
        self.idPadre = idPadre

    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            menus = conexion.obtener("SELECT id, nombre, estado, idPadre FROM conf_menus WHERE estado = 1")
            return menus
        finally:
            conexion.cerrar()