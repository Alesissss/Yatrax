import bd
import hashlib

class TipoServicio:
    def __init__(self, idTipoServicio = None, nombre = None, descripcion = None, estado = None, estadoProceso = None, estadoRegistro = None, fechaRegistro = None, usuario = None):
        self.idTipoCliente = idTipoServicio
        self.nombre = nombre
        self.descripcion = descripcion
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
            tipos_servicio = conexion.obtener("Select idTipoServicio as ID, nombre as TIPO, descripcion, estado from tipo_servicio where estado_registro = 1")
            return tipos_servicio
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, idTipoServicio):
        try:
            conexion = bd.Conexion()
            tipo_servicio = conexion.obtener("Select idTipoServicio as ID, nombre, descripcion, estado from tipo_servicio where estado_registro = 1 and idTipoServicio =  %s", (idTipoServicio,))
            return tipo_servicio[0] if tipo_servicio else None
        finally:
                conexion.cerrar()

    @classmethod
    def eliminar_tipo_servicio(cls, idTipoServicio):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_ELIMINAR_TIPO_SERVICIO(%s);", (idTipoServicio,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()
    
    @classmethod
    def registrar(cls, nombre, descripcion, estado, usuario):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_INSERTAR_TIPO_SERVICIO(%s, %s, %s, %s);", (nombre, estado, descripcion, usuario))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()

    @classmethod
    def editar(cls, idTipoServicio, nombre, descripcion, estado):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_ACTUALIZAR_TIPO_SERVICIO(%s, %s, %s, %s)", (idTipoServicio, nombre, descripcion, estado))
            resultado = conexion.obtener("SELECT @MSJ, @MS2J;")
            return resultado[0]
        finally:
            conexion.cerrar()
    
    @classmethod
    def darBaja(cls, idTipoServicio):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_DAR_BAJA_TIPO_SERVICIO(%s)", (idTipoServicio,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()
            