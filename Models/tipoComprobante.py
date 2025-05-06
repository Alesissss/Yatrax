import bd
import hashlib

class TipoComprobante:
    def __init__(self, idTipoComprobante = None, nombre = None, estado = None, estadoProceso = None, estadoRegistro = None, fechaRegistro = None, usuario = None):
        self.idTipoCliente = idTipoComprobante
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
            tipos_comprobante = conexion.obtener("Select idTipoComprobante as ID, nombre as TIPO, estado from tipo_comprobante where estado_registro = 1")
            return tipos_comprobante
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, idTipoComprobante):
        try:
            conexion = bd.Conexion()
            tipo_comprobante = conexion.obtener("Select idTipoComprobante as ID, nombre, estado from tipo_comprobante where estado_registro = 1 and idTipoComprobante =  %s", (idTipoComprobante,))
            return tipo_comprobante[0] if tipo_comprobante else None
        finally:
                conexion.cerrar()

    @classmethod
    def eliminar_tipo_comprobante(cls, idTipoComprobante):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_ELIMINAR_TIPO_COMPROBANTE(%s);", (idTipoComprobante,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()
    
    @classmethod
    def registrar(cls, nombre, estado, usuario):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_INSERTAR_TIPO_COMPROBANTE(%s, %s, %s);", (nombre, estado, usuario))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()

    @classmethod
    def editar(cls, idTipoComprobante, nombre, estado):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_ACTUALIZAR_TIPO_COMPROBANTE(%s, %s, %s)", (idTipoComprobante, nombre, estado))
            resultado = conexion.obtener("SELECT @MSJ, @MS2J;")
            return resultado[0]
        finally:
            conexion.cerrar()
    
    @classmethod
    def darBaja(cls, idTipoComprobante):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_DAR_BAJA_TIPO_COMPROBANTE(%s)", (idTipoComprobante,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()
            