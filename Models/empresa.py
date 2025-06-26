import bd

class Empresa:
    def __init__(self, id=None, razon_social=None, ruc=None, direccion=None, telefono=None, email=None, estado=1, fecha_registro=None, usuario=None):
        self.id = id
        self.razon_social = razon_social
        self.ruc = ruc
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.estado = estado
        self.fecha_registro = fecha_registro
        self.usuario = usuario
    
    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            query = """
                SELECT id, razon_social, ruc, direccion, telefono, email, estado, fecha_registro, usuario
                FROM empresa
            """
            return conexion.obtener(query)
        finally:
            conexion.cerrar()
    
    @classmethod
    def obtener_por_id(cls, id):
        conexion = bd.Conexion()
        try:
            query = """
                SELECT id, razon_social, ruc, direccion, telefono, email, estado, fecha_registro, usuario
                FROM empresa
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
                SELECT id, razon_social, ruc, direccion, telefono, email, estado, fecha_registro, usuario
                FROM empresa
                WHERE estado = 1
            """
            return conexion.obtener(query)
        finally:
            conexion.cerrar()

    @classmethod
    def registrar(cls, razon_social, ruc, direccion, telefono, email, usuario_actual):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar(
                "CALL SP_REGISTRAR_EMPRESA(%s, %s, %s, %s, %s, %s);",
                (razon_social, ruc, direccion, telefono, email, usuario_actual)
            )
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()

    @classmethod
    def editar(cls, id, razon_social, ruc, direccion, telefono, email, usuario_actual):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar(
                "CALL SP_EDITAR_EMPRESA(%s, %s, %s, %s, %s, %s, %s);",
                (id, razon_social, ruc, direccion, telefono, email, usuario_actual)
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
                "CALL SP_ELIMINAR_EMPRESA(%s);",
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
                "CALL SP_ACTIVAR_EMPRESA(%s);",
                (id,)
            )
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()
