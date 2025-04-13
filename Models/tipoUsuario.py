import bd

class TipoUsuario:
    def __init__(self, id=None, nombre=None, estadoProceso=None, estadoRegistro=None, fechaRegistro=None, usuario=None):
        self.id = id
        self.nombre = nombre
        #Auditoría
        self.estadoProceso = estadoProceso
        self.estadoRegistro = estadoRegistro
        self.fechaRegistro = fechaRegistro
        self.usuario = usuario

    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            tipo_usuarios = conexion.obtener("SELECT * FROM tipo_usuario where estado_registro = 1")
            return tipo_usuarios
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, tipoUsuario_id):
        conexion = bd.Conexion()
        try:
            tipo_usuario = conexion.obtener("SELECT * FROM tipo_usuario WHERE estado_registro = 1 AND id = %s", (tipoUsuario_id,))
            return tipo_usuario[0] if tipo_usuario else None
        finally:
            conexion.cerrar()

    #REGISTRAR
    @classmethod
    def registrar(cls, nombre, usuario):
        conexion = bd.Conexion()
        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_REGISTRAR_TIPO_USUARIO(%s, %s);", (nombre, usuario))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()