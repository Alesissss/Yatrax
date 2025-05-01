import bd
import hashlib

class TipoCliente:
    def __init__(self, idTipoCliente = None, nombre = None, estado = None):
        self.idTipoCliente = idTipoCliente
        self.nombre = nombre
        self.estado = estado

    @classmethod
    def obtener_datos(cls):
        try:
            conexion = bd.Conexion()
            listado = conexion.obtener("""
            SELECT 
                idTipoCliente AS id,
                nombre as tipo,
                CAST(estado AS UNSIGNED) AS ESTADO
            FROM tipo_cliente
            """)
            return listado
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def obtenerUno(cls, idTipoCliente):
        try:
            conexion = bd.Conexion()
            listado = conexion.obtener("""
            SELECT 
                idTipoCliente AS id,
                nombre,
                CAST(estado AS UNSIGNED) AS ESTADO
            FROM tipo_cliente where idTipoCliente = %s
            """,(idTipoCliente,))
            return listado[0] if listado else None
        except Exception as e:
            print(f"Error en obtener uno: {str(e)}")
            raise
        finally:
            if conexion:
                conexion.cerrar()
    
    @classmethod
    def insertarTipoCliente(cls, nombre):
        try:
            conexion = bd.Conexion()
            cursor = conexion.conn.cursor()
            cursor.callproc('SP_INSERTAR_TIPO_CLIENTE', (nombre, 1))
            conexion.conn.commit()
        except Exception as e:
            print(f"Error al insertar tipo cliente: {str(e)}")
            raise
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

    @classmethod
    def actualizarTipoCliente(cls, idTipoCliente, nombre, estado):
        try:
            conexion = bd.Conexion()
            cursor = conexion.conn.cursor()
            cursor.callproc('SP_ACTUALIZAR_TIPO_CLIENTE', (idTipoCliente, nombre, estado))
            conexion.conn.commit()
        except Exception as e:
            print(f"Error al actualizar tipo cliente: {str(e)}")
            raise
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()
    
    @classmethod
    def darBajaTipoCliente(cls, idTipoCliente):
        try:
            conexion = bd.Conexion()
            cursor = conexion.conn.cursor()
            cursor.callproc('SP_DAR_BAJA_TIPO_CLIENTE', (idTipoCliente,))
            conexion.conn.commit()
        except Exception as e:
            print(f"Error al dar de baja tipo cliente: {str(e)}")
            raise
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()
