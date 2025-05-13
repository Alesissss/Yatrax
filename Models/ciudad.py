import bd

class Ciudad:
    def __init__(self, id=None, nombre=None, abreviatura=None):
        self.id = id
        self.nombre = nombre
        self.abreviatura = abreviatura
        
    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            return conexion.obtener("SELECT id, nombre, abreviatura FROM ciudad")
        finally:
            conexion.cerrar()
    
    @classmethod
    def obtener_abreviatura(cls, nombre):
        conexion = bd.Conexion()
        try:
            resultado = conexion.obtener("SELECT abreviatura FROM ciudad WHERE nombre = %s", (nombre,))
            return resultado[0] if resultado else None
        finally:
            conexion.cerrar()