import bd

class MetodoPago:
    def __init__(self, id=None, nombre=None, logo=None, estado=None):
        self.id = id
        self.nombre = nombre
        self.logo = logo
        self.estado = estado

    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            return conexion.obtener("SELECT id, nombre, logo, estado FROM metodo_pago")
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, metodo_pago_id):
        conexion = bd.Conexion()
        try:
            resultado = conexion.obtener("SELECT id, nombre, logo, estado FROM metodo_pago WHERE id = %s", (metodo_pago_id,))
            return resultado[0] if resultado else None
        finally:
            conexion.cerrar()

    @classmethod
    def registrar(cls, nombre, logo, estado):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("INSERT INTO metodo_pago (nombre, logo, estado) VALUES (%s, %s, %s)", (nombre, logo, estado))
            return {"Status": "success", "Msj": "Método de pago registrado exitosamente"}
        finally:
            conexion.cerrar()

    @classmethod
    def editar(cls, id, nombre, logo, estado):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("UPDATE metodo_pago SET nombre = %s, logo = %s, estado = %s WHERE id = %s", (nombre, logo, estado, id))
            return {"Status": "success", "Msj": "Método de pago editado exitosamente"}
        finally:
            conexion.cerrar()

    @classmethod
    def eliminar(cls, id):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("DELETE FROM metodo_pago WHERE id = %s", (id,))
            return {"Status": "success", "Msj": "Método de pago eliminado exitosamente"}
        finally:
            conexion.cerrar()
