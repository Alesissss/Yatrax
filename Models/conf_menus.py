import hashlib
import bd

class Conf_Menus:
    def __init__(self, id=None, nombre=None, estado=None):
        self.id = id
        self.nombre = nombre
        self.estado = estado

    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            menus = conexion.obtener("SELECT id, nombre, estado FROM conf_menus WHERE estado = 1")
            return menus
        finally:
            conexion.cerrar()