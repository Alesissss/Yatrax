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
                    m.id as id_marca,
                    m.nombre AS marca,
                    s.id as id_servicio,
                    s.nombre AS servicio,
                    tv.cantidad,
                    tv.estado
                FROM tipo_vehiculo tv
                LEFT JOIN marca m ON tv.id_marca = m.id
                LEFT JOIN servicio s ON tv.id_servicio = s.id 
                GROUP BY 
                    tv.id, 
                    tv.nombre,
                    m.id,
                    m.nombre,
                    s.id,
                    s.nombre,
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
                    id_servicio,
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
    def insertarTipoVehiculo(cls, nombre, idmarca, cantidad, estado, servicio, usuario):
        conexion = None
        try:
            conexion = bd.Conexion()
            conexion.ejecutar('CALL SP_INSERTAR_TIPOVEHICULO(%s,%s,%s,%s,%s,%s)', (nombre,idmarca,cantidad,estado,servicio,usuario))
            resultado = conexion.obtener("SELECT @MSJ;")
            return resultado[0]    
        except Exception as e:
            print(f"Error en insertarTipoVehiculo: {str(e)}")
            raise
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def actualizarTipoVehiculo(cls,id,nombre,marca,estado,cantidad,servicio, usuario):
        conexion = None
        try:
            conexion = bd.Conexion()
            conexion.ejecutar("CALL SP_ACTUALIZAR_TIPOVEHICULO(%s,%s,%s,%s,%s,%s,%s,@MSJ,@MSJ2)",(id,nombre,marca,estado,cantidad,servicio,usuario))
            resultado = conexion.obtener("SELECT @MSJ AS MSJ, @MSJ2 AS MSJ2;")
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

