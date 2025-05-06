import bd

class Sucursal:
    def __init__(self, id=None, ubigeo=None, nombre=None, direccion=None, latitud=None, longitud=None, estado=1, estado_proceso='REGISTRADO', estado_registro=1, fecha_registro=None, usuario=None):
        self.id = id
        self.ubigeo = ubigeo
        self.nombre = nombre
        self.direccion = direccion
        self.latitud = latitud
        self.longitud = longitud
        self.estado = estado
        #Auditoría
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
                FROM sucursal WHERE estado_registro = 1
            """
            return conexion.obtener(query)
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, id):
        conexion = bd.Conexion()
        try:
            query = """
                SELECT id, ubigeo, nombre, direccion, latitud, longitud, estado, 
                       estado_proceso, estado_registro, fecha_registro, usuario
                FROM sucursal WHERE estado_registro = 1 AND id = %s 
            """
            resultado = conexion.obtener(query, (id,))
            return resultado[0] if resultado else None
        finally:
            conexion.cerrar()

    #LOGIN
    @classmethod
    def autenticar(cls, email, password):
            conexion = bd.Conexion()
            try:
                usuario = conexion.obtener("SELECT usu.id, usu.nombre, usu.email, usu.imagen, usu.estado, usu.id_tipousuario, tu.nombre as tipousuario"
                " FROM usuarios usu INNER JOIN tipo_usuario tu on usu.id_tipousuario = tu.id WHERE usu.estado_registro = 1 AND usu.estado = 1 AND usu.email = %s AND usu.password = %s", (email, password))
                return usuario[0] if usuario else None
            finally:
                conexion.cerrar()

    @classmethod
    def registrar(cls, ubigeo, nombre, direccion, latitud, longitud, usuario):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar(
                "CALL SP_REGISTRAR_SUCURSAL(%s, %s, %s, %s, %s, %s);",
                (ubigeo, nombre, direccion, latitud, longitud, usuario)
            )
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()

    @classmethod
    def editar(cls, id, ubigeo, direccion, nombre, latitud, longitud, usuario):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar(
                "CALL SP_EDITAR_SUCURSAL(%s, %s, %s, %s, %s, %s, %s);",
                (id, ubigeo, nombre, direccion, latitud, longitud, usuario)
            )
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()

    @classmethod
    def eliminar(cls, id, usuario):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_ELIMINAR_SUCURSAL(%s, %s);", (id, usuario,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()

    @classmethod
    def dar_baja(cls, id, usuario):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_DARBAJA_SUCURSAL(%s);", (id, usuario,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()
