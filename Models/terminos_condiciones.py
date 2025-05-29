import bd

class TerminosCondiciones:
    def __init__(self, id=None, nombre=None, archivo=None, estado=1, fecha_registro=None, usuario=None):
        self.id = id
        self.nombre = nombre
        self.archivo = archivo
        self.estado = estado
        self.fecha_registro = fecha_registro
        self.usuario = usuario
    
    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            query = """
                SELECT id, nombre, archivo, estado, fecha_registro, usuario
                FROM terminos_condiciones
            """
            return conexion.obtener(query)
        finally:
            conexion.cerrar()
            
    @classmethod
    def obtener_por_id(cls, id):
        conexion = bd.Conexion()
        try:
            query = """
                SELECT id, nombre, archivo, estado, fecha_registro, usuario
                FROM terminos_condiciones
                WHERE id = %s
            """
            resultado = conexion.obtener(query, (id,))
            return resultado[0] if resultado else None
        finally:
            conexion.cerrar()
            
    @classmethod
    def obtener_activos(cls):
        conexion = bd.Conexion()
        try:
            query = """
                SELECT id, nombre, archivo, estado, fecha_registro, usuario
                FROM terminos_condiciones
                WHERE estado = 1
            """
            return conexion.obtener(query)
        finally:
            conexion.cerrar()
    
    @classmethod
    def registrar(cls, nombre, archivo, usuario_actual):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar(
                "CALL SP_REGISTRAR_TERMINOS_CONDICIONES(%s, %s, %s);",
                (nombre, archivo, usuario_actual)
            )
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
            
        finally:
            conexion.cerrar()
            
    @classmethod
    def editar(cls, id, nombre, archivo, usuario_actual):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar(
                "CALL SP_EDITAR_TERMINOS_CONDICIONES(%s, %s, %s, %s);",
                (id, nombre, archivo, usuario_actual)
            )
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
            
        finally:
            conexion.cerrar()
            
    @classmethod
    def eliminar(cls, id):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar(
                "CALL SP_ELIMINAR_TERMINOS_CONDICIONES(%s);",
                (id,)
            )
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()
            
    @classmethod
    def activar(cls, id):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar(
                "CALL SP_ACTIVAR_TERMINOS_CONDICIONES(%s);",
                (id,)
            )
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()
