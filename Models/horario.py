import hashlib
import bd

class horario:
    def __init__(self, id=None, horario_entrada=None, horario_salida=None, estado=None, estado_proceso=None, estado_registro=None, fecha_registro=None):
        self.id = id,
        self.horario_entrada = horario_entrada,
        self.horario_salida = horario_salida,
        self.estado = estado,
        #Auditoría
        self.estado_proceso = estado_proceso,
        self.estado_registro = estado_registro
        self.fecha_registro = fecha_registro

    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            horario = conexion.obtener("SELECT id, horario_entrada, horario_salida, estado, estado_proceso FROM horario")
            return horario
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, horario_id):
        conexion = bd.Conexion()
        try:
            horario = conexion.obtener(f"SELECT id, horario_entrada, horario_salida, estado, estado_proceso FROM horario WHERE id = {horario_id}")
            return horario[0] if horario else None
        finally:
            conexion.cerrar()

    #REGISTRAR
    @classmethod
    def registrar(cls,horario_entrada, horario_salida, estado,estado_registro=1):
        conexion = bd.Conexion()
        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_REGISTRAR_horario(%s, %s, %s, %s, %s, %s);", (nombre, email, password_hash, imagen, idTipohorario, horario))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()

    #EDITAR
    @classmethod
    def editar(cls, id, nombre, email, imagen, idTipohorario):
        conexion = bd.Conexion()

        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_EDITAR_horario(%s, %s, %s, %s, %s);", (id, nombre, email, imagen, idTipohorario))

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
            conexion.ejecutar("CALL SP_ELIMINAR_horario(%s);", (id, ))

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
            conexion.ejecutar("CALL SP_DARBAJA_horario(%s);", (id, ))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()