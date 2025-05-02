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
            usuarios = conexion.obtener("SELECT usu.id, usu.nombre, usu.email, usu.imagen, usu.estado, usu.id_tipousuario, tu.nombre as tipousuario"
            " FROM usuarios usu INNER JOIN tipo_usuario tu on usu.id_tipousuario = tu.id WHERE usu.estado_registro = 1")
            return usuarios
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, usuario_id):
        conexion = bd.Conexion()
        try:
            usuario = conexion.obtener("SELECT usu.id, usu.nombre, usu.email, usu.imagen, usu.estado, usu.id_tipousuario, tu.nombre as tipousuario"
            " FROM usuarios usu INNER JOIN tipo_usuario tu on usu.id_tipousuario = tu.id WHERE usu.estado_registro = 1 AND usu.id = %s", (usuario_id,))
            return usuario[0] if usuario else None
        finally:
            conexion.cerrar()

    #LOGIN
    @classmethod
    def autenticar(cls, email, password):
        conexion = bd.Conexion()
        try:
            usuario = conexion.obtener("SELECT usu.id, usu.nombre, usu.email, usu.imagen, usu.estado, usu.id_tipousuario, tu.nombre as tipousuario"
            " FROM usuarios usu INNER JOIN tipo_usuario tu on usu.id_tipousuario = tu.id WHERE usu.estado_registro = 1 AND usu.estado = 1 AND usu.email = %s AND usu.password = %s", (email, password))
            return usuario[0] if usuario else None
        finally:
            conexion.cerrar()

    #OBTENER MENÚS
    @classmethod
    def obtener_menus(cls, id):
        conexion = bd.Conexion()
        try:
            menus = conexion.obtener("SELECT men.id, men.nombre"
            " FROM conf_menus men INNER JOIN conf_dmenus dmen on dmen.idMenu = men.id WHERE dmen.idUsuario = %s AND men.estado = 1", (id))
            return menus
        finally:
            conexion.cerrar()

    #ASIGNAR DMENU
    @classmethod
    def agregar_menu(cls, idMenu, idUsuario):
        conexion = bd.Conexion()

        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_ASIGNAR_DMENU(%s, %s);", (idMenu, idUsuario))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()

    #ELIMINAR DMENU
    @classmethod
    def eliminar_menu(cls, idMenu, idUsuario):
        conexion = bd.Conexion()

        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_ELIMINAR_DMENU(%s, %s);", (idMenu, idUsuario))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()

    #REGISTRAR
    @classmethod
    def registrar(cls, nombre, email, password, imagen, estado, idTipoUsuario, usuario):
        conexion = bd.Conexion()

        try:
            password_hash = hashlib.sha256(password.encode()).hexdigest()

            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_REGISTRAR_USUARIO(%s, %s, %s, %s, %s, %s, %s);", (nombre, email, password_hash, imagen, estado, idTipoUsuario, usuario))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()

    #EDITAR
    @classmethod
    def editar(cls, id, nombre, email, imagen, estado, idTipoUsuario):
        conexion = bd.Conexion()

        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_EDITAR_USUARIO(%s, %s, %s, %s, %s, %s);", (id, nombre, email, imagen, estado, idTipoUsuario))

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