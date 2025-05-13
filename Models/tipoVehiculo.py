import bd
import hashlib

class TipoVehiculo:
    def __init__(self,idTipoVehiculo=None,nombre=None,idMarca=None,estado=None,cantidad=None):
        self.idTipoVehiculo=idTipoVehiculo
        self.nombre=nombre
        self.idMarca=idMarca
        self.estado=estado
        self.cantidad=cantidad

    @classmethod
    def obtener_todos(cls):
        try:
            conexion = bd.Conexion()
            listado = conexion.obtener("""
                SELECT 
                    tv.id AS id,
                    tv.nombre AS nombre,
                    COALESCE(SUM(CASE WHEN n.estado = 1 THEN n.cantidad ELSE 0 END), 0) AS capacidad,
                    m.nombre AS marca,
                    tv.cantidad,
                    tv.estado
                FROM tipo_vehiculo tv
                LEFT JOIN nivel n ON tv.id = n.id_tipo_vehiculo
                LEFT JOIN marca m ON tv.id_marca = m.id
                GROUP BY 
                    tv.id, 
                    tv.nombre, 
                    m.nombre, 
                    tv.cantidad, 
                    tv.estado;
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
                    id AS id,
                    nombre,
                    id_marca,
                    cantidad,
                    estado
                FROM tipo_vehiculo where id=%s
            """,(idTipoVehiculo,))
            return listado[0] if listado else None
        except Exception as e:
            print(f"Error en obtenerUno: {str(e)}")
            raise
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def insertarTipoVehiculo(cls, nombre, idmarca,cantidad):
        conexion = None
        try:
            conexion = bd.Conexion()
            conexion.ejecutar('CALL SP_INSERTAR_TIPOVEHICULO(%s,%s,%s,@MSJ)', (nombre,idmarca,cantidad))
            resultado = conexion.obtener("SELECT @MSJ;")
            return resultado[0]    
        except Exception as e:
            print(f"Error en insertarTipoVehiculo: {str(e)}")
            raise
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def actualizarTipoVehiculo(cls,id,nombre,marca,estado,cantidad):
        conexion = None
        try:
            conexion = bd.Conexion()
            conexion.ejecutar("CALL SP_ACTUALIZAR_TIPOVEHICULO(%s,%s,%s,%s,%s,@mensaje, @error)",(id,nombre,marca,estado,cantidad))
            resultado = conexion.obtener("SELECT @mensaje AS MSJ, @error AS MSJ2;")
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

