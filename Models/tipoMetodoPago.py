import bd
import hashlib

class TipoMetodoPago:
    def __init__(self, idTipoMetodoPago = None, nombre = None, estado = None, fechaRegistro = None, usuario = None):
        self.idTipoCliente = idTipoMetodoPago
        self.nombre = nombre
        self.estado = estado
        #Auditoría
        self.fechaRegistro = fechaRegistro
        self.usuario = usuario

    @classmethod
    def obtener_todos(cls):
        try:
            conexion = bd.Conexion()
            tipos_servicio = conexion.obtener("Select idTipoMetodoPago as ID, nombre as NOMBRE, estado from tipo_metodoPago")
            return tipos_servicio
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, idTipoMetodoPago):
        try:
            conexion = bd.Conexion()
            tipo_metodoPago = conexion.obtener("Select idTipoMetodoPago as ID, nombre, estado from tipo_metodoPago where idTipoMetodoPago =  %s", (idTipoMetodoPago,))
            print(tipo_metodoPago)
            return tipo_metodoPago[0]
        finally:
                conexion.cerrar()

    
    @staticmethod
    def registrar(nombre, estado, usuario):
        try:
            conexion = bd.Conexion()
            conexion.ejecutar("CALL SP_INSERTAR_TIPO_METODOPAGO(%s, %s, %s)", (nombre, estado, usuario))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2")
            return resultado[0]
        finally:
            conexion.cerrar()

    @staticmethod
    def editar(id, nombre, estado, usuario):
        try:
            conexion = bd.Conexion()
            conexion.ejecutar("CALL SP_ACTUALIZAR_TIPO_METODOPAGO(%s,%s,%s,%s)", (id, nombre, estado, usuario))
            resultado=conexion.obtener("SELECT @MSJ, @MSJ2")
            return resultado[0]
        finally:
            conexion.cerrar()

    @staticmethod
    def darBaja(id, usuario):
        try:
            conexion = bd.Conexion()
            conexion.ejecutar("CALL SP_DAR_BAJA_TIPO_METODOPAGO(%s,%s)", (id, usuario))
            resultado=conexion.obtener("SELECT @MSJ, @MSJ2")
            return resultado[0]
        finally:
            conexion.cerrar()

    @staticmethod
    def eliminar(id):
        try:
            conexion = bd.Conexion()
            conexion.ejecutar("CALL SP_ELIMINAR_TIPO_METODOPAGO(%s)", (id))
            resultado=conexion.obtener("SELECT @MSJ, @MSJ2")
            return resultado[0]
        finally:
            conexion.cerrar()
            