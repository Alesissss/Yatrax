import bd

class Sucursal:
    def __init__(self, id=None, departamento=None, nombre=None, direccion=None, latitud=None, longitud=None, estado=1, estado_proceso='REGISTRADO', estado_registro=1, fecha_registro=None, usuario=None):
        self.id = id
        self.departamento = departamento
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
                SELECT id, departamento, nombre, direccion, latitud, longitud, estado, 
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
                SELECT id, departamento, nombre, direccion, latitud, longitud, estado, 
                       estado_proceso, estado_registro, fecha_registro, usuario
                FROM sucursal WHERE id = %s and estado_registro = 1
            """
            resultado = conexion.obtener(query, (id,))
            return resultado[0] if resultado else None
        finally:
            conexion.cerrar()

    @classmethod
    def registrar(cls, departamento, nombre, direccion, latitud, longitud, usuario_actual):
        conexion = bd.Conexion()
        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar(
                "CALL SP_REGISTRAR_SUCURSAL(%s, %s, %s, %s, %s, %s);",
                (departamento, nombre, direccion, latitud, longitud, usuario_actual)
            )
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
            
        finally:
            conexion.cerrar()

    @classmethod
    def editar(cls, id, departamento, direccion, nombre, latitud, longitud, usuario):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar(
                "CALL SP_EDITAR_SUCURSAL(%s, %s, %s, %s, %s, %s, %s);",
                (id, departamento, nombre, direccion, latitud, longitud, usuario)
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
