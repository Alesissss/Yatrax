import bd

class Sucursal:
    def __init__(self, id=None, ubigeo=None, nombre=None, latitud=None, longitud=None,
                 estado='A', estado_proceso='REGISTRADO', estado_registro=1, 
                 fecha_registro=None, usuario=None):
        self.id = id
        self.ubigeo = ubigeo
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud
        self.estado = estado
        self.estado_proceso = estado_proceso
        self.estado_registro = estado_registro
        self.fecha_registro = fecha_registro
        self.usuario = usuario

    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            query = """
                SELECT id, ubigeo, nombre, direccion, latitud, longitud, estado, 
                       estado_proceso, estado_registro, fecha_registro, usuario
                FROM sucursal
            """
            return conexion.obtener(query)
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, id):
        conexion = bd.Conexion()
        try:
            query = """
                SELECT id, ubigeo, nombre, direcion, latitud, longitud, estado, 
                       estado_proceso, estado_registro, fecha_registro, usuario
                FROM sucursal WHERE id = %s
            """
            resultado = conexion.obtener(query, (id,))
            return resultado[0] if resultado else None
        finally:
            conexion.cerrar()

    @classmethod
    def registrar(cls, ubigeo, nombre, latitud, longitud, usuario):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar(
                "CALL SP_REGISTRAR_SUCURSAL(%s, %s, %s, %s, %s);",
                (ubigeo, nombre, latitud, longitud, usuario)
            )
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()

    @classmethod
    def editar(cls, id, ubigeo, nombre, latitud, longitud):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar(
                "CALL SP_EDITAR_SUCURSAL(%s, %s, %s, %s, %s);",
                (id, ubigeo, nombre, latitud, longitud)
            )
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()

    @classmethod
    def eliminar(cls, id):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_ELIMINAR_SUCURSAL(%s);", (id,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()

    @classmethod
    def dar_baja(cls, id):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_DARBAJA_SUCURSAL(%s);", (id,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()
