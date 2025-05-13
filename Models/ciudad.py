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
            
    @classmethod
    def registrar_abreviatura(cls, nombre, abreviatura):
        conexion = bd.Conexion()
        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar(
                "CALL SP_REGISTRAR_ABREVIATURA_CIUDAD(%s, %s);",
                (nombre, abreviatura)
            )
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()