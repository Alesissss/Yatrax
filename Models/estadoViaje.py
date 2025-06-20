import bd

class EstadoViaje:
    def __init__(self, id=None, nombre=None):
        self.id = id
        self.nombre = nombre

    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            asientos = conexion.obtener("""
                SELECT id, nombre FROM estado_viaje;
            """)
            return asientos
        finally:
            conexion.cerrar()