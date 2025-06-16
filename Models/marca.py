import bd

class Marca:
    def __init__(self, id=None, nombre=None, estado=None):
        self.id = id
        self.nombre = nombre
        self.estado = estado

    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            return conexion.obtener("SELECT id, nombre, logo , estado FROM marca")
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, marca_id):
        conexion = bd.Conexion()
        try:
            resultado = conexion.obtener("SELECT id, nombre, logo, estado FROM marca WHERE id = %s", (marca_id,))
            return resultado[0] if resultado else None
        finally:
            conexion.cerrar()

    @classmethod
    def registrar(cls, nombre,logo, estado, usuario):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_REGISTRAR_MARCA(%s, %s,%s, %s)", (nombre, logo, estado, usuario))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()

    @classmethod
    def editar(cls, id, nombre, estado, logo):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_EDITAR_MARCA(%s, %s, %s, %s)", (id, nombre, estado, logo))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()

    @classmethod
    def eliminar(cls, id):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_ELIMINAR_MARCA(%s)", (id,))
            return {"Status": "success", "Msj": "Marca eliminada exitosamente"}
        finally:
            conexion.cerrar()

    @classmethod
    def darBaja(cls, id):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_DARBAJA_MARCA(%s)", (id,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()
