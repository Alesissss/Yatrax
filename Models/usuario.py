import hashlib
import bd

class Usuario:
    def __init__(self, id=None, nombre=None, email=None, password=None, id_tipoUsuario=None, fechaRegistro=None, usuario=None):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.password = password
        self.id_tipoUsuario = id_tipoUsuario
        #Auditoría
        self.fechaRegistro = fechaRegistro
        self.usuario = usuario

    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            usuarios = conexion.obtener(""" SELECT usu.id, CONCAT(pe.ape_paterno, ' ', pe.ape_materno, ', ', pe.nombre) AS nombre, usu.email, usu.imagen, usu.estado, usu.id_tipousuario, tu.nombre as tipousuario, pe.id as id_personal
            FROM usuarios usu
            INNER JOIN tipo_usuario tu ON usu.id_tipousuario = tu.id
            INNER JOIN personal pe ON pe.id = usu.id_personal""")
            return usuarios
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, usuario_id):
        conexion = bd.Conexion()
        try:
            usuario = conexion.obtener(""" SELECT usu.id, CONCAT(pe.ape_paterno, ' ', pe.ape_materno, ', ', pe.nombre) AS nombre, usu.email, usu.imagen, usu.estado, usu.id_tipousuario, tu.nombre as tipousuario, pe.id as id_personal
            FROM usuarios usu
            INNER JOIN tipo_usuario tu ON usu.id_tipousuario = tu.id
            INNER JOIN personal pe ON pe.id = usu.id_personal WHERE usu.id = %s""", (usuario_id,))
            return usuario[0] if usuario else None
        finally:
            conexion.cerrar()

    #LOGIN
    @classmethod
    def autenticar(cls, email, password):
        conexion = bd.Conexion()
        try:
            usuario = conexion.obtener(""" SELECT usu.id, CONCAT(pe.ape_paterno, ' ', pe.ape_materno, ', ', pe.nombre) AS nombre, usu.email, usu.imagen, usu.estado, 
            usu.id_tipousuario, tu.nombre as tipousuario, pe.id as id_personal, tp.id as id_tipopersonal, tp.nombre as tipoPersonal
            FROM usuarios usu
            INNER JOIN tipo_usuario tu ON usu.id_tipousuario = tu.id
            INNER JOIN personal pe ON pe.id = usu.id_personal 
            INNER JOIN tipo_personal tp ON tp.id = pe.id_tipopersonal WHERE usu.estado = 1 AND usu.email = %s AND usu.password = %s""", (email, password))
            return usuario[0] if usuario else None
        finally:
            conexion.cerrar()

    #REGISTRAR
    @classmethod
    def registrar(cls, idPersonal, email, password, imagen, estado, idTipoUsuario, usuario):
        conexion = bd.Conexion()

        try:
            password_hash = hashlib.sha256(password.encode()).hexdigest()

            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_REGISTRAR_USUARIO(%s, %s, %s, %s, %s, %s, %s);", (idPersonal, email, password_hash, imagen, estado, idTipoUsuario, usuario))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()

    #EDITAR
    @classmethod
    def editar(cls, id, idPersonal, email, imagen, estado, idTipoUsuario):
        conexion = bd.Conexion()

        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_EDITAR_USUARIO(%s, %s, %s, %s, %s, %s);", (id, idPersonal, email, imagen, estado, idTipoUsuario))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()
    
    @classmethod
    def actualizar_contrasena(cls,email,contrasena):
        conexion = bd.Conexion()

        try:
            clave_hasheada = hashlib.sha256(contrasena.encode()).hexdigest()
            conexion.ejecutar("CALL SP_CAMBIAR_CLAVE(%s,%s,@MSJ,@MSJ2);", (email,clave_hasheada, ))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
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