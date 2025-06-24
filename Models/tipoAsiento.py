import bd

class TipoAsiento:
    def __init__(self, id=None, nombre=None, icono=None, id_tipo=None):
        self.id = id
        self.nombre = nombre
        self.icono = icono
        self.id_tipo = id_tipo

    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            query = """
                SELECT id, nombre, icono, precio, id_tipo
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
                SELECT id, nombre, icono, precio, id_tipo
                FROM herramienta WHERE id_tipo = 1 AND id = %s
            """
            resultado = conexion.obtener(query, (id,))
            return resultado[0] if resultado else None
        finally:
            conexion.cerrar()

    @classmethod
    def registrar(cls, ciudad, nombre, direccion, latitud, longitud, estado, abreviatura, usuario_actual):
        conexion = bd.Conexion()
        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar(
                "CALL SP_REGISTRAR_SUCURSAL(%s, %s, %s, %s, %s, %s, %s, %s);",
                (ciudad, nombre, direccion, latitud, longitud, estado, abreviatura, usuario_actual)
            )
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
            
        finally:
            conexion.cerrar()

    @classmethod
    def editar(cls, id, ciudad, nombre, direccion, latitud, longitud, estado, abreviatura, usuario):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar(
                "CALL SP_EDITAR_SUCURSAL(%s, %s, %s, %s, %s, %s, %s, %s, %s);",
                (id, ciudad, nombre, direccion, latitud, longitud, estado, abreviatura, usuario)
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
            conexion.ejecutar("CALL SP_DARBAJA_SUCURSAL(%s, %s);", (id, usuario,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()
