import hashlib
import bd

class Personal:
    def __init__(self, id=None, nombre=None, ape_paterno=None, ape_materno=None, email=None, password=None, imagen=None, estado=None, id_tipoPersonal=None, estadoProceso=None, estadoRegistro=None, fechaRegistro=None, usuario=None):
        self.id = id
        self.nombre = nombre
        self.ape_paterno = ape_paterno
        self.ape_materno = ape_materno
        self.email = email
        self.password = password
        self.imagen = imagen
        self.estado = estado
        self.id_tipoPersonal = id_tipoPersonal
        # Auditoría
        self.fechaRegistro = fechaRegistro
        self.usuario = usuario

    # Obtener todos los registros de personal
    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            personal = conexion.obtener("SELECT per.id, per.nombre, per.ape_paterno, per.ape_materno, per.imagen, per.estado, per.id_tipopersonal, tp.nombre as tipopersonal"
                                        " FROM personal per INNER JOIN tipo_personal tp on per.id_tipopersonal = tp.id")
            return personal
        finally:
            conexion.cerrar()

    # Obtener un registro de personal por su ID
    @classmethod
    def obtener_por_id(cls, personal_id):
        conexion = bd.Conexion()
        try:
            personal = conexion.obtener("SELECT per.id, per.nombre, per.ape_paterno, per.ape_materno, per.imagen, per.estado, per.id_tipopersonal, tp.nombre as tipopersonal"
                                        " FROM personal per INNER JOIN tipo_personal tp on per.id_tipopersonal = tp.id WHERE per.id = %s", (personal_id,))
            return personal[0] if personal else None
        finally:
            conexion.cerrar()

    # Registrar un nuevo personal
    @classmethod
    def registrar(cls, nombre, apePat, apeMat, imagen, estado, idTipoPersonal, usuario):
        conexion = bd.Conexion()
        try:

            # Llamar al procedimiento almacenado para registrar el personal
            conexion.ejecutar("CALL SP_REGISTRAR_PERSONAL(%s, %s, %s, %s, %s, %s, %s);", (nombre, apePat, apeMat, imagen, estado, idTipoPersonal, usuario))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()

    # Editar un registro de personal
    @classmethod
    def editar(cls, id, nombre, apePat, apeMat, imagen, estado, idTipoPersonal):
        conexion = bd.Conexion()
        try:
            # Llamar al procedimiento almacenado para editar el personal
            conexion.ejecutar("CALL SP_EDITAR_PERSONAL(%s, %s, %s, %s, %s, %s, %s);", (id, nombre, apePat, apeMat, imagen, estado, idTipoPersonal))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()

    # Eliminar un registro de personal
    @classmethod
    def eliminar(cls, id):
        conexion = bd.Conexion()
        try:
            # Llamar al procedimiento almacenado para eliminar el personal
            conexion.ejecutar("CALL SP_ELIMINAR_PERSONAL(%s);", (id,))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()

    # Dar de baja un personal (cambiar estado)
    @classmethod
    def darBaja(cls, id):
        conexion = bd.Conexion()
        try:
            # Llamar al procedimiento almacenado para dar de baja el personal
            conexion.ejecutar("CALL SP_DARBAJA_PERSONAL(%s);", (id,))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()

    @classmethod
    def verificarViaje(cls, id):
        conexion = bd.Conexion()
        try:
            result = conexion.obtener(""" SELECT v.id FROM viaje v
                            INNER JOIN detalle_personal dp ON v.id = dp.idViaje 
                            WHERE dp.idPersonal = %s AND v.estado = 1 AND v.idEstadoViaje = 2 LIMIT 1 """, (id,))
            
            return result[0] if result else None
        finally:
            conexion.cerrar()
