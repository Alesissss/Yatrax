import bd
import hashlib

class MicroServicio:
    def __init__(self, id, nombre, descripcion, estado, fechaRegistro, usuario):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado
        self.fechaRegistro = fechaRegistro
        self.usuario = usuario

    @classmethod
    def obtener_todos(cls):
        try:
            conexion = bd.Conexion()
            microservicios = conexion.obtener(""" SELECT s.id AS id, s.nombre AS nombre, s.descripcion AS descripcion, s.estado FROM microservicio s """)
            return microservicios
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_uno(cls, id):
        try:
            conexion = bd.Conexion()
            microservicio = conexion.obtener("SELECT s.id AS id, s.nombre AS nombre, s.descripcion AS descripcion, s.estado FROM microservicio s WHERE id = %s", (id,))
            return microservicio[0] if microservicio else None
        finally:
            conexion.cerrar()

    @classmethod
    def registrar(cls, nombre, descripcion, estado, usuario):
        try:
            conexion = bd.Conexion()
            conexion.ejecutar("CALL SP_INSERTAR_MICROSERVICIO(%s, %s, %s, %s)", (nombre, descripcion, estado, usuario))
            mensajes = conexion.obtener("SELECT @MSJ, @MSJ2")
            return mensajes[0]
        except Exception as e:
            print("Ha ocurrido un error al registrar un servicio: " + repr(e))
        finally:
            conexion.cerrar()

    @classmethod
    def editar(cls, id, nombre, descripcion, estado):
        try:
            conexion = bd.Conexion()
            conexion.ejecutar("CALL SP_ACTUALIZAR_MICROSERVICIO(%s, %s, %s, %s)", (id, nombre, descripcion, estado))
            mensajes = conexion.obtener("SELECT @MSJ, @MSJ2")
            return mensajes[0]
        except Exception as e:
            print("Ha ocurrido un error al editar un servicio: " + repr(e))
        finally:
            conexion.cerrar()

    @classmethod
    def darBaja(cls, id):
        try:
            conexion = bd.Conexion()
            conexion.ejecutar("CALL SP_DAR_BAJA_MICROSERVICIO(%s)", (id,))
            mensajes = conexion.obtener("SELECT @MSJ, @MSJ2")
            return mensajes[0]
        except Exception as e:
            print("Ha ocurrido un error al dar de baja un servicio: " + repr(e))
        finally:
            conexion.cerrar()

    @classmethod
    def eliminar(cls, id):
        try:
            conexion = bd.Conexion()
            conexion.ejecutar("CALL SP_ELIMINAR_MICROSERVICIO(%s)", (id,))
            mensajes = conexion.obtener("SELECT @MSJ, @MSJ2")
            return mensajes[0]
        except Exception as e:
            print("Ha ocurrido un error al eliminar un servicio: " + repr(e))
        finally:
            conexion.cerrar()
    @classmethod
    def obtenerPorServicio(cls,id):
        conexion = bd.Conexion()
        try:
            datos_microServicio = conexion.obtener("""
            SELECT 
                m.id as ms_id,
                m.nombre as ms_nombre
            FROM servicio s
            INNER JOIN servicio_microservicio sm ON s.id = sm.idServicio
            INNER JOIN microservicio m ON m.id = sm.idMicroservicio
            WHERE s.id = %s AND m.estado = 1;
                             """,(id,))
            return datos_microServicio
        finally:
            conexion.cerrar()
