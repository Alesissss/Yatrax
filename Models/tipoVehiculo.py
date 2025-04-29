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
                    largo,
                    ancho,
                    capacidad,
                    combustible,
                    consumo,
                    CAST(estado AS UNSIGNED) AS estado  -- Convertir BIT a entero
                FROM tipo_vehiculo
            """)
            return listado
        finally:
            conexion.cerrar()

    @classmethod
    def insertarTipoVehiculo(cls,nombre,largo,ancho,capacidad,combustible,consumo):
        try:
            conexion = bd.Conexion()
            conexion = conexion.ejecutar("CALL SP_INSERTAR_TIPO_VEHICULO(%s,%s,%s,%s,%s,%s);",(nombre,largo,ancho,capacidad,combustible,consumo))
        finally:
            conexion.cerrar()

    @classmethod
    def actualizarTipoVehiculo(cls,id,nombre,largo,ancho,capacidad,combustible,consumo):
        try:
            conexion = bd.Conexion()
            conexion = conexion.ejecutar("CALL SP_ACTUALIZAR_TIPO_VEHICULO(%s,%s,%s,%s,%s,%s,%s);",(id,nombre,largo,ancho,capacidad,combustible,consumo))
        finally:
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

