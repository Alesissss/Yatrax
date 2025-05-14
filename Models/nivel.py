import bd
import hashlib

class Nivel:
    def __init__(self, idNivel=None, nroPiso=None, vehiculo=None, cantidad=None, estado=None):
        self.idNivel = idNivel
        self.nroPiso = nroPiso
        self.vehiculo = vehiculo
        self.cantidad = cantidad
        self.estado = estado

    @classmethod
    def obtener_todos(cls):
        conexion = None
        try:
            conexion = bd.Conexion()
            listado = conexion.obtener("""
                SELECT 
                n.id AS id,
                n.nroPiso,
                v.placa AS placa,
                n.cantidad,
                n.estado
            FROM 
                nivel n
            INNER JOIN 
                vehiculo v ON n.id_vehiculo = v.id;
            """)
            return listado
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def obtener_uno_por_idNivel(cls, idNivel):
        conexion = None
        try:
            conexion = bd.Conexion()
            listado = conexion.obtener(
                "SELECT * FROM nivel WHERE id = %s",
                (idNivel,)
            )
            return listado[0]
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def obtener_por_tipo_vehiculo(cls, vehiculo):
        conexion = None
        try:
            conexion = bd.Conexion()
            listado = conexion.obtener(
                "SELECT * FROM nivel WHERE id_vehiculo = %s ORDER BY nroPiso",
                (vehiculo,)
            )
            return listado
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def insertar_nivel(cls, vehiculo, cantidad):
        conexion = None
        try:
            conexion = bd.Conexion()
            conexion.ejecutar(
                "CALL SP_INSERTAR_NIVEL(%s, %s)",
                (vehiculo, cantidad)
            )
            resultado = conexion.obtener("SELECT @MSJ AS MSJ, @MSJ2 AS MSJ2;")
            return resultado[0]["MSJ"], resultado[0]["MSJ2"]  # (mensaje_exito, mensaje_error)
        except Exception as e:
            print(f"Error en insertar_nivel: {e}")
            raise
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def actualizar_nivel(cls, idNivel, nroPiso, vehiculo, cantidad,estado):
        conexion = None
        try:
            conexion = bd.Conexion()
            conexion.ejecutar(
                "CALL SP_ACTUALIZAR_NIVEL(%s, %s, %s, %s,%s)",
                (idNivel, nroPiso, vehiculo, cantidad,estado)
            )
            resultado = conexion.obtener("SELECT @MSJ as MSJ, @MSJ2 as MSJ2;")
            return resultado[0]["MSJ"], resultado[0]["MSJ2"]
        except Exception as e:
            print(f"Error en actualizar_nivel: {e}")
            raise
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def dar_baja_piso(cls, idNivel):
        conexion = None
        try:
            conexion = bd.Conexion()
            conexion.ejecutar(
                "CALL SP_DARBAJA_PISO(%s)",
                (idNivel,)
            )
            resultado = conexion.obtener("SELECT @MSJ AS MSJ, @MSJ2 AS MSJ2;")
            return resultado[0]["MSJ"], resultado[0]["MSJ2"]
        except Exception as e:
            print(f"Error en dar_baja_piso: {e}")
            raise
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def eliminar_nivel(cls, idNivel):
        conexion = None
        try:
            conexion = bd.Conexion()
            conexion.ejecutar(
                "CALL SP_ELIMINAR_NIVEL(%s)",
                (idNivel,)
            )
            resultado = conexion.obtener("SELECT @MSJ as MSJ, @MSJ2 as MSJ2;")
            return resultado[0]["MSJ"], resultado[0]["MSJ2"]
        except Exception as e:
            print(f"Error en eliminar_nivel: {e}")
            raise
        finally:
            if conexion:
                conexion.cerrar()