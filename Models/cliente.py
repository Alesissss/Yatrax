import hashlib
import bd

class Cliente:
    def __init__(self, id=None, id_pais=None,id_tipo_doc=None,id_tipo_cliente=None, numero_documento=None, nombres=None, ape_paterno = None, ape_materno = None, email=None,sexo =None,f_nacimiento = None,razon_social = None, direccion=None, password=None, telefono=None, fechaRegistro=None, usuario=None):
        self.id = id
        self.id_pais=id_pais
        self.id_tipo_doc = id_tipo_doc
        self.id_tipo_cliente = id_tipo_cliente
        self.numero_documento = numero_documento
        self.nombres = nombres
        self.ape_paterno = ape_paterno
        self.ape_materno = ape_materno
        self.sexo = sexo
        self.f_nacimiento = f_nacimiento
        self.razon_social = razon_social
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.password = password
        #Auditoría
        self.fechaRegistro = fechaRegistro
        self.usuario = usuario

    @classmethod    
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            clientes = conexion.obtener("")
            return clientes
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, usuario_id):
        conexion = bd.Conexion()
        try:
            usuario = conexion.obtener("SELECT usu.id, usu.nombres, usu.email, usu.imagen, usu.estado, usu.id_tipousuario, tu.nombres as tipousuario"
                " FROM usuarios usu INNER JOIN tipo_usuario tu on usu.id_tipousuario = tu.id WHERE usu.estado_registro = 1 AND usu.id = %s", (usuario_id,))
            return usuario[0] if usuario else None
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