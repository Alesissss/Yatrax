import bd
import hashlib

class Servicio:
    def __init__(self, id, nombre, descripcion, estado, fechaRegistro, usuario, imagen):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado
        self.fechaRegistro = fechaRegistro
        self.usuario = usuario
        self.imagen = imagen

    @classmethod
    def obtener_todos(cls):
        try:
            conexion = bd.Conexion()
            servicios = conexion.obtener("""
                SELECT s.id AS id, s.nombre AS nombre, s.descripcion AS descripcion,
                       s.estado AS estado, s.imagen AS imagen
                FROM servicio s
            """)
            print(servicios)
            return servicios
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_uno(cls, id):
        try:
            conexion = bd.Conexion()
            servicio = conexion.obtener("""
                SELECT s.id AS id, s.nombre AS nombre, s.descripcion AS descripcion,
                       s.estado, s.fecha_registro AS fechaRegistro, s.usuario, s.imagen
                FROM servicio s
                WHERE s.id = %s
            """, (id,))
            return servicio[0] if servicio else None
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_micros_por_servicio(cls, id):
        try:
            conexion = bd.Conexion()
            micros = conexion.obtener("""
                SELECT m.id, m.nombre, m.descripcion, m.estado,
                       sm.idServicio as idServicio
                FROM microservicio m
                INNER JOIN servicio_microservicio sm ON m.id = sm.idMicroservicio
                WHERE sm.idServicio = %s
            """, (id,))
            return micros
        finally:
            conexion.cerrar()

    @classmethod
    def registrar(cls, nombre, descripcion, estado, usuario, imagen, microservicios):
        try:
            conexion = bd.Conexion()
            conexion.ejecutar(
                "CALL SP_INSERTAR_SERVICIO(%s, %s, %s, %s, %s)",
                (nombre, descripcion, estado, usuario, imagen),
                auto_commit=False
            )

            mensajes = conexion.obtener("SELECT @MSJ, @MSJ2, LAST_INSERT_ID() AS idServicio;")
            idServicio = mensajes[0]['idServicio']
            msj2 = mensajes[0]['@MSJ2']

            if msj2:
                raise Exception('Error al registrar servicio: ' + msj2)

            for m in microservicios:
                conexion.ejecutar(
                    "INSERT INTO servicio_microservicio (idServicio, idMicroservicio, usuario) VALUES (%s, %s, %s)",
                    (idServicio, m['id'], usuario),
                    auto_commit=False
                )

            conexion.conn.commit()
            return mensajes[0]

        except Exception as e:
            conexion.conn.rollback()
            return {'@MSJ': '', '@MSJ2': f'Error al ejecutar la transacción de registro de servicio: {repr(e)}'}
        finally:
            conexion.cerrar()

    @classmethod
    def editar(cls, id, nombre, descripcion, estado, imagen, usuario, microservicios):
        try:
            conexion = bd.Conexion()
            conexion.ejecutar(
                "CALL SP_ACTUALIZAR_SERVICIO(%s, %s, %s, %s, %s)",
                (id, nombre, descripcion, estado, imagen),
                auto_commit=False
            )

            mensajes = conexion.obtener("SELECT @MSJ, @MSJ2")
            msj2 = mensajes[0]['@MSJ2']

            if msj2:
                raise Exception('Error al registrar servicio: ' + msj2)

            conexion.ejecutar(
                "DELETE FROM servicio_microservicio WHERE idServicio = %s",
                (id,),
                auto_commit=False
            )

            for m in microservicios:
                conexion.ejecutar(
                    "INSERT INTO servicio_microservicio (idServicio, idMicroservicio, usuario) VALUES (%s, %s, %s)",
                    (id, m['id'], usuario),
                    auto_commit=False
                )

            conexion.conn.commit()
            return mensajes[0]

        except Exception as e:
            conexion.conn.rollback()
            return {'@MSJ': '', '@MSJ2': f'Error al ejecutar la transacción de registro de servicio: {repr(e)}'}
        finally:
            conexion.cerrar()

    @classmethod
    def darBaja(cls, id):
        try:
            conexion = bd.Conexion()
            conexion.ejecutar("CALL SP_BAJA_SERVICIO(%s)", (id,))
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
            conexion.ejecutar("CALL SP_DELETE_SERVICIO(%s)", (id,))
            mensajes = conexion.obtener("SELECT @MSJ, @MSJ2")
            return mensajes[0]
        except Exception as e:
            print("Ha ocurrido un error al eliminar un servicio: " + repr(e))
        finally:
            conexion.cerrar()
