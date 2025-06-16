import bd
import hashlib

class TipoCliente:
    def __init__(self, idTipoCliente = None, nombre = None, estado = None, fechaRegistro = None, usuario = None):
        self.idTipoCliente = idTipoCliente
        self.nombre = nombre
        self.estado = estado
        #Auditoría
        self.fechaRegistro = fechaRegistro
        self.usuario = usuario

    @classmethod
    def obtener_todos(cls):
        try:
            conexion = bd.Conexion()
            tipos_cliente = conexion.obtener("Select idTipoCliente as ID, nombre as TIPO, estado from tipo_cliente")
            return tipos_cliente
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, idTipoCliente):
        try:
            conexion = bd.Conexion()
            tipo_cliente = conexion.obtener("Select idTipoCliente as ID, nombre, estado from tipo_cliente where idTipoCliente =  %s", (idTipoCliente,))
            return tipo_cliente[0] if tipo_cliente else None
        finally:
                conexion.cerrar()

    @classmethod
    def obtener_por_nombre(cls, nombre):
        try:
            conexion = bd.Conexion()
            tipo_cliente = conexion.obtener("Select idTipoCliente as ID, nombre, estado from tipo_cliente where UPPER(nombre) = UPPER(%s)", (nombre,))
            return tipo_cliente[0] if tipo_cliente else None
        finally:
                conexion.cerrar()
    
    @classmethod
    def eliminar_tipo_cliente(cls, idTipoCliente):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_ELIMINAR_TIPO_CLIENTE(%s);", (idTipoCliente,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()
    
    @classmethod
    def registrar(cls, nombre, estado, usuario):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_INSERTAR_TIPO_CLIENTE(%s, %s, %s);", (nombre, estado, usuario))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()

    @classmethod
    def editar(cls, idTipoCliente, nombre, estado):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_ACTUALIZAR_TIPO_CLIENTE(%s, %s, %s)", (idTipoCliente, nombre, estado))
            resultado = conexion.obtener("SELECT @MSJ, @MS2J;")
            return resultado[0]
        finally:
            conexion.cerrar()
    
    @classmethod
    def darBaja(cls, idTipoCliente):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_DAR_BAJA_TIPO_CLIENTE(%s)", (idTipoCliente,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()
            