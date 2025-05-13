import bd
import hashlib

class Servicio:
    def __init__(self, idServicio, nombre, descripcion, idTipoServicio, estado):
        self.idServicio = idServicio
        self.nombre = nombre
        self.descripcion = descripcion
        self.idTipoServicio = idTipoServicio
        self.estado = estado

    @classmethod
    def obtener_todos(cls):
        try:
            conexion = bd.Conexion()
            listado = conexion.obtener("""
                    SELECT
                        s.id AS id,
                        s.nombre AS nombre,
                        s.descripcion AS descripcion,
                        tpser.nombre AS idTipoServicio,
                        s.estado AS estado
                    FROM servicio s 
                    LEFT JOIN tipo_servicio tpser ON s.id_tipo_servicio = tpser.idTipoServicio
            """)
            return listado
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def obtener_unServicio(cls, idServicio):
        try:
            conexion = bd.Conexion()
            servicio = conexion.obtener("SELECT * FROM servicio WHERE id = %s", (idServicio,))
            return servicio[0]
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def insertarServicio(cls, nombre, descripcion, idTipoServicio):
        try:
            conexion = bd.Conexion()
            resultado = conexion.ejecutar("CALL SP_INSERTAR_SERVICIO(%s, %s, %s)", (nombre, descripcion, idTipoServicio))
            result = resultado.fetchall()
            return result
        except Exception as e:
            print("Ha ocurrido un error al insertar un servicio: " + repr(e))
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def actualizarServicio(cls, idServicio, nombre, descripcion, idTipoServicio, estado):
        try:
            conexion = bd.Conexion()
            resultado = conexion.ejecutar("CALL SP_ACTUALIZAR_SERVICIO(%s, %s, %s, %s, %s)",
                                          (idServicio, nombre, descripcion, idTipoServicio, estado))
            result = resultado.fetchall()
            return result
        except Exception as e:
            print("Ha ocurrido un error al actualizar un servicio: " + repr(e))
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def darBajaServicio(cls, idServicio):
        try:
            conexion = bd.Conexion()
            resultado = conexion.ejecutar("CALL SP_BAJA_SERVICIO(%s)", (idServicio,))
            result = resultado.fetchall()
            return result
        except Exception as e:
            print("Ha ocurrido un error al dar de baja un servicio: " + repr(e))
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def eliminarServicio(cls, idServicio):
        try:
            conexion = bd.Conexion()
            resultado = conexion.ejecutar("CALL SP_DELETE_SERVICIO(%s)", (idServicio,))
            result = resultado.fetchall()
            return result
        except Exception as e:
            print("Ha ocurrido un error al eliminar un servicio: " + repr(e))
        finally:
            if conexion:
                conexion.cerrar()
