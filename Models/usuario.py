import hashlib
import bd

class Usuario:
    def __init__(self, id=None, nombre=None, email=None, password=None, id_tipoUsuario=None, estadoProceso=None, estadoRegistro=None, fechaRegistro=None, usuario=None):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.password = password
        self.id_tipoUsuario = id_tipoUsuario
        #Auditoría
        self.estadoProceso = estadoProceso
        self.estadoRegistro = estadoRegistro
        self.fechaRegistro = fechaRegistro
        self.usuario = usuario

    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            usuarios = conexion.obtener("SELECT usu.id, usu.nombre, usu.email, usu.imagen, usu.estado_registro, usu.id_tipousuario, tu.nombre as tipousuario"
            " FROM usuarios usu INNER JOIN tipo_usuario tu on usu.id_tipousuario = tu.id")
            return usuarios
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, usuario_id):
        conexion = bd.Conexion()
        try:
            usuario = conexion.obtener("SELECT usu.id, usu.nombre, usu.email, usu.imagen, usu.id_tipousuario, tu.nombre as tipousuario"
            " FROM usuarios usu INNER JOIN tipo_usuario tu on usu.id_tipousuario = tu.id WHERE usu.id = %s", (usuario_id,))
            return usuario[0] if usuario else None
        finally:
            conexion.cerrar()

    #LOGIN
    @classmethod
    def autenticar(cls, email, password):
        conexion = bd.Conexion()
        try:
            usuario = conexion.obtener("SELECT usu.id, usu.nombre, usu.email, usu.imagen, usu.id_tipousuario, tu.nombre as tipousuario"
            " FROM usuarios usu INNER JOIN tipo_usuario tu on usu.id_tipousuario = tu.id WHERE usu.estado_registro = 1 AND usu.email = %s AND usu.password = %s", (email, password))
            return usuario[0] if usuario else None
        finally:
            conexion.cerrar()

    #REGISTRAR
    @classmethod
    def registrar(cls, nombre, email, password, imagen, idTipoUsuario, usuario):
        conexion = bd.Conexion()

        try:
            password_hash = hashlib.sha256(password.encode()).hexdigest()

            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_REGISTRAR_USUARIO(%s, %s, %s, %s, %s, %s);", (nombre, email, password_hash, imagen, idTipoUsuario, usuario))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()

    #EDITAR
    @classmethod
    def editar(cls, id, nombre, email, imagen, idTipoUsuario):
        conexion = bd.Conexion()

        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_EDITAR_USUARIO(%s, %s, %s, %s, %s);", (id, nombre, email, imagen, idTipoUsuario))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()
    
    #ELIMINAR
    @classmethod
    def eliminar(cls, id):
        conexion = bd.Conexion()

        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_ELIMINAR_USUARIO(%s);", (id, ))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()

    #DAR DE BAJA
    @classmethod
    def darBaja(cls, id):
        conexion = bd.Conexion()

        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_DARBAJA_USUARIO(%s);", (id, ))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()