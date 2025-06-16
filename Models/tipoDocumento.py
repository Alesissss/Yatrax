import bd

class TipoDocumento:
    def __init__(self, id = None, nombre = None, abreviatura = None, estado = None, fechaRegistro = None, usuario = None):
        self.id = id
        self.nombre = nombre
        self.abreviatura = abreviatura
        self.estado = estado
        #Auditoría
        self.fechaRegistro = fechaRegistro
        self.usuario = usuario
        
    @classmethod
    def obtener_todos(cls):
        try:
            conexion = bd.Conexion()
            tipos_documento = conexion.obtener("Select id , nombre , abreviatura , estado from tipo_documento ")
            return tipos_documento
        finally:
            conexion.cerrar()
    
    @classmethod
    def obtener_por_id(cls, idTipoDocumento):
        try:
            conexion = bd.Conexion()
            tipo_documento = conexion.obtener("Select id , nombre, abreviatura, estado from tipo_documento where id =  %s", (idTipoDocumento,))
            return tipo_documento[0] if tipo_documento else None
        finally:
                conexion.cerrar()
                
    @classmethod
    def eliminar_tipo_documento(cls, idTipoDocumento):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_ELIMINAR_TIPO_DOCUMENTO(%s);", (idTipoDocumento,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()
            
    @classmethod
    def registrar(cls, nombre, abreviatura, estado, usuario):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_REGISTRAR_TIPO_DOCUMENTO(%s, %s, %s, %s);", (nombre, abreviatura, estado, usuario))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()
    
    @classmethod
    def editar(cls, idTipoDocumento, nombre, abreviatura, estado):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_EDITAR_TIPO_DOCUMENTO(%s, %s, %s, %s)", (idTipoDocumento, nombre, abreviatura, estado))
            resultado = conexion.obtener("SELECT @MSJ, @MS2J;")
            return resultado[0]
        finally:
            conexion.cerrar()
            
    @classmethod
    def darBaja(cls, idTipoDocumento):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_DARBAJA_TIPO_DOCUMENTO(%s);", (idTipoDocumento,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()
