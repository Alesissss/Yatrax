import bd

class TipoUsuario:
    def __init__(self, id=None, nombre=None, estado=None, fechaRegistro=None, usuario=None):
        self.id = id
        self.nombre = nombre
        self.estado = estado
        #Auditoría
        self.fechaRegistro = fechaRegistro
        self.usuario = usuario

    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            tipo_usuarios = conexion.obtener("SELECT * FROM tipo_usuario where")
            return tipo_usuarios
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, tipoUsuario_id):
        conexion = bd.Conexion()
        try:
            tipo_usuario = conexion.obtener("SELECT * FROM tipo_usuario WHERE id = %s", (tipoUsuario_id,))
            return tipo_usuario[0] if tipo_usuario else None
        finally:
            conexion.cerrar()

    #OBTENER MENÚS
    @classmethod
    def obtener_menus(cls, idTipoUsuario):
        conexion = bd.Conexion()
        try:
            menus = conexion.obtener("SELECT men.id, men.nombre"
            " FROM conf_menus men INNER JOIN conf_dmenus dmen on dmen.idMenu = men.id WHERE dmen.idTipoUsuario = %s AND men.estado = 1", (idTipoUsuario))
            return menus
        finally:
            conexion.cerrar()
    
    #ASIGNAR DMENU
    @classmethod
    def agregar_menu(cls, idMenu, idTipoUsuario):
        conexion = bd.Conexion()

        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_ASIGNAR_DMENU(%s, %s);", (idMenu, idTipoUsuario))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()

    #ELIMINAR DMENU
    @classmethod
    def eliminar_menu(cls, idMenu, idTipoUsuario):
        conexion = bd.Conexion()

        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_ELIMINAR_DMENU(%s, %s);", (idMenu, idTipoUsuario))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()

    #OBTENER CLAIMS
    @classmethod
    def obtener_claims(cls, idTipoUsuario):
        conexion = bd.Conexion()
        try:
            menus = conexion.obtener("SELECT c.id, c.nombre"
            " FROM conf_dclaims dc INNER JOIN conf_claims c on dc.idClaim = c.id WHERE dc.idTipoUsuario = %s AND c.estado = 1", (idTipoUsuario))
            return menus
        finally:
            conexion.cerrar()
    
    #ASIGNAR DCLAIM
    @classmethod
    def agregar_claim(cls, idClaim, idTipoUsuario):
        conexion = bd.Conexion()

        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_ASIGNAR_DCLAIM(%s, %s);", (idClaim, idTipoUsuario))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()

    #ELIMINAR DCLAIM
    @classmethod
    def eliminar_claim(cls, idClaim, idTipoUsuario):
        conexion = bd.Conexion()

        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_ELIMINAR_DCLAIM(%s, %s);", (idClaim, idTipoUsuario))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()

    #REGISTRAR
    @classmethod
    def registrar(cls, nombre, estado, usuario):
        conexion = bd.Conexion()
        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_REGISTRAR_TIPO_USUARIO(%s, %s, %s);", (nombre, estado, usuario))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()

    #EDITAR
    @classmethod
    def editar(cls, id, nombre, estado):
        conexion = bd.Conexion()

        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_EDITAR_TIPO_USUARIO(%s, %s, %s);", (id, nombre, estado))

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
            conexion.ejecutar("CALL SP_ELIMINAR_TIPO_USUARIO(%s);", (id, ))

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
            conexion.ejecutar("CALL SP_DARBAJA_TIPO_USUARIO(%s);", (id, ))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()