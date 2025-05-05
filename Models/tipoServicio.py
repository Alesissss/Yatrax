import bd
import hashlib

class TipoCliente:
    def __init__(self, idTipoServicio = None, nombre = None, estado = None, estadoProceso = None, estadoRegistro = None, fechaRegistro = None, usuario = None):
        self.idTipoCliente = idTipoServicio
        self.nombre = nombre
        self.estado = estado
        #Auditoría
        self.estadoProceso = estadoProceso
        self.estadoRegistro = estadoRegistro
        self.fechaRegistro = fechaRegistro
        self.usuario = usuario

    @classmethod
    def obtener_todos(cls):
        try:
            conexion = bd.Conexion()
            tipos_cliente = conexion.obtener("Select idTipoServicio as ID, nombre as TIPO, estado from tipo_cliente where estado_registro = 1")
            return tipos_cliente
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, idTipoServicio):
        try:
            conexion = bd.Conexion()
            tipo_cliente = conexion.obtener("Select idTipoServicio as ID, nombre, estado from tipo_cliente where estado_registro = 1 and idTipoCliente =  %s", (idTipoServicio,))
            return tipo_cliente[0] if tipo_cliente else None
        finally:
                conexion.cerrar()

    @classmethod
    def eliminar_tipo_cliente(cls, idTipoServicio):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_ELIMINAR_TIPO_CLIENTE(%s);", (idTipoServicio,))
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
    def editar(cls, idTipoServicio, nombre, estado):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_ACTUALIZAR_TIPO_CLIENTE(%s, %s, %s)", (idTipoServicio, nombre, estado))
            resultado = conexion.obtener("SELECT @MSJ, @MS2J;")
            return resultado[0]
        finally:
            conexion.cerrar()
    
    @classmethod
    def darBaja(cls, idTipoServicio):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_DAR_BAJA_TIPO_CLIENTE(%s)", (idTipoServicio,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()
            