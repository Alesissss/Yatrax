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
            return conexion.obtener("SELECT id, nombre, logo, estado, qr , id_tipo_metodoPago FROM metodo_pago where estado_registro = 1")
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, metodo_pago_id):
        conexion = bd.Conexion()
        try:
            resultado = conexion.obtener("SELECT id, nombre, logo, estado, qr , id_tipo_metodoPago FROM metodo_pago WHERE id = %s", (metodo_pago_id,))
            return resultado[0] if resultado else None
        finally:
            conexion.cerrar()

    @classmethod
    def registrar(cls, nombre, logo, estado, usuario,tipo_pago, qr):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_REGISTRAR_METODO_PAGO(%s, %s, %s, %s,%s,%s)", (nombre, logo, estado, usuario, tipo_pago, qr))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()

    @classmethod
    def editar(cls, id, nombre, logo, estado, tipo_pago , qr):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_EDITAR_METODO_PAGO(%s, %s, %s, %s,%s,%s)", (id,nombre, logo, estado,tipo_pago, qr))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()

    @classmethod
    def eliminar(cls, id):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_ELIMINAR_METODO_PAGO(%s)", (id,))
            return {"Status": "success", "Msj": "Método de pago eliminado exitosamente"}
        finally:
            conexion.cerrar()

    @classmethod
    def darBaja(cls, id):
        conexion = bd.Conexion()
        try:
            # Usamos el procedimiento almacenado para dar de baja el método de pago
            conexion.ejecutar("CALL SP_DARBAJA_METODO_PAGO(%s)", (id,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()