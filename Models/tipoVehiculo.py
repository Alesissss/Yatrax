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
    def insertarTipoVehiculo(cls, nombre, capacidad):
        conexion = None
        try:
            conexion = bd.Conexion()
            conexion.ejecutar('CALL SP_INSERTAR_TIPOVEHICULO(%s,%s,@MSJ, @MSJ2)', (nombre,capacidad))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]        
        except Exception as e:
            print(f"Error en insertarTipoVehiculo: {str(e)}")
            raise
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def actualizarTipoVehiculo(cls,id,nombre,capacidad,estado):
        conexion = None
        try:
            conexion = bd.Conexion()
            conexion.ejecutar("CALL SP_ACTUALIZAR_TIPOVEHICULO(%s,%s,%s,%s,@MSJ, @MSJ2)",(id,nombre,capacidad,estado))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def darBajaTipoVehiculo(cls, idTipoVehiculo):
        conexion = None
        try:
            conexion = bd.Conexion()
            conexion.ejecutar("CALL SP_DARBAJA_TIPOVEHICULO(%s,@MSJ, @MSJ2)", (idTipoVehiculo,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def eliminarTipoVehiculo(cls, idTipoVehiculo):
        conexion = None
        try:
            conexion = bd.Conexion()
            conexion.ejecutar("CALL SP_ELIMINAR_TIPOVEHICULO(%s,@MSJ, @MSJ2)", (idTipoVehiculo,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            if conexion:
                conexion.cerrar()

