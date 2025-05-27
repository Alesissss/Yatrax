import bd
import hashlib

class Sancion:
    def __init__(self, id = None, nombre = None, descripcion = None, duracion_sancion = None, estado = None, fecha_registro = None, usuario = None):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.duracion_sancion = duracion_sancion
        self.estado = estado
        self.fechaRegistro = fecha_registro
        self.usuario = usuario

    @classmethod
    def obtener_todos(cls):
        try:
            conexion = bd.Conexion()
            sancion = conexion.obtener("Select id as ID, nombre, descripcion, duracion_sancion, estado from incidencia")
            return sancion
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, id):
        try:
            conexion = bd.Conexion()
            sancion = conexion.obtener("Select id as ID, nombre, descripcion, duracion_sancion, estado from incidencia where id =  %s", (id,))
            return sancion[0] if sancion else None
        finally:
                conexion.cerrar()

    @classmethod
    def eliminar_sancion(cls, id):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_ELIMINAR_INCIDENCIA(%s);", (id,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()
    
    @classmethod
    def registrar(cls, nombre, descripcion, duracion_sancion, estado, usuario):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_REGISTRAR_INCIDENCIA(%s, %s, %s, %s, %s);", (nombre, descripcion, duracion_sancion, estado, usuario))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()

    @classmethod
    def editar(cls, id, nombre, descripcion, duracion_sancion, estado):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_EDITAR_INCIDENCIA(%s, %s, %s, %s, %s)", (id, nombre, descripcion, duracion_sancion, estado))
            resultado = conexion.obtener("SELECT @MSJ, @MS2J;")
            return resultado[0]
        finally:
            conexion.cerrar()
    
    @classmethod
    def darBaja(cls, id):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_DARBAJA_INCIDENCIA(%s)", (id,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()
            