import bd
import hashlib

class TipoVehiculo:
    def __init__(self,idTipoVehiculo=None,nombre=None,largo=None,ancho=None,capacidad=None,combustible=None,consumo=None,estado=None):
        self.idTipoVehiculo=idTipoVehiculo
        self.nombre=nombre
        self.largo=largo
        self.ancho=ancho
        self.capacidad=capacidad
        self.combustible=combustible
        self.consumo=consumo
        self.estado=estado

    @classmethod
    def obtener_todos(cls):
        try:
            conexion = bd.Conexion()
            listado = conexion.obtener("""
                SELECT 
                    idTipoVehiculo AS id,
                    nombre,
                    capacidad,
                    estado
                FROM tipo_vehiculo
            """)
            return listado
        finally:
            conexion.cerrar()

    @classmethod
    def obtenerUno(cls,idTipoVehiculo):
        try:
            conexion = bd.Conexion()
            listado = conexion.obtener("""
                SELECT 
                    idTipoVehiculo AS id,
                    nombre,
                    capacidad,
                    estado
                FROM tipo_vehiculo where idTipoVehiculo=%s
            """,(idTipoVehiculo,))
            return listado[0] if listado else None
        except Exception as e:
            print(f"Error en obtenerUno: {str(e)}")
            raise
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def insertarTipoVehiculo(cls, nombre, capacidad, estado):
        conexion = None
        cursor = None
        try:
            conexion = bd.Conexion()
            cursor = conexion.conn.cursor()
            cursor.callproc('SP_INSERTAR_TIPOVEHICULO', (nombre,capacidad,estado))
            conexion.conn.commit()
        except Exception as e:
            print(f"Error en insertarTipoVehiculo: {str(e)}")
            raise
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.cerrar()

    @classmethod
    def actualizarTipoVehiculo(cls,id,nombre,capacidad,estado):
        conexion = None
        try:
            conexion = bd.Conexion()
            conexion = conexion.ejecutar("CALL SP_ACTUALIZAR_TIPOVEHICULO(%s,%s,%s,%s);",(id,nombre,capacidad,estado))
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def darBajaTipoVehiculo(cls, idTipoVehiculo):
        conexion = None
        try:
            conexion = bd.Conexion()  # Creas la conexión
            resultado = conexion.ejecutar("CALL SP_ELIMINAR_TIPO_VEHICULO(%s);", (idTipoVehiculo,))
            # No sobrescribes 'conexion', todo bien
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def eliminarTipoVehiculo(cls, idTipoVehiculo):
        conexion = None
        try:
            conexion = bd.Conexion()  # Creas la conexión
            resultado = conexion.ejecutar("CALL SP_ELIMINAR_TIPOVEHICULO(%s);", (idTipoVehiculo,))
            # No sobrescribes 'conexion', todo bien
        finally:
            if conexion:
                conexion.cerrar()

