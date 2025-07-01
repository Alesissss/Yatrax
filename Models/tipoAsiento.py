import bd

class TipoAsiento:
    def __init__(self, id=None, nombre=None, icono=None, precio=None, estado=None, id_tipo=None):
        self.id = id
        self.nombre = nombre
        self.icono = icono
        self.precio = precio
        self.estado = estado
        self.id_tipo = id_tipo

    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            query = """
                SELECT id, nombre, icono, precio, estado, id_tipo
                FROM herramienta WHERE id_tipo = 1
            """
            return conexion.obtener(query)
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, id):
        conexion = bd.Conexion()
        try:
            query = """
                SELECT id, nombre, icono, precio, estado, id_tipo
                FROM herramienta WHERE id_tipo = 1 AND id = %s
            """
            resultado = conexion.obtener(query, (id,))
            return resultado[0] if resultado else None
        finally:
            conexion.cerrar()

    @classmethod
    def registrar(cls, nombre, icono, precio, estado):
        conexion = bd.Conexion()
        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar(
                "CALL SP_REGISTRAR_TIPO_ASIENTO(%s, %s, %s, %s);",
                (nombre, icono, precio, estado)
            )
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
            
        finally:
            conexion.cerrar()

    @classmethod
    def editar(cls, id, nombre, icono, precio, estado):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar(
                "CALL SP_EDITAR_TIPO_ASIENTO(%s, %s, %s, %s, %s);",
                (id, nombre, icono, precio, estado)
            )
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()

    @classmethod
    def dar_baja(cls, id):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_DARBAJA_TIPO_ASIENTO(%s);", (id,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()

    @classmethod
    def eliminar(cls, id):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_ELIMINAR_TIPO_ASIENTO(%s);", (id,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()
