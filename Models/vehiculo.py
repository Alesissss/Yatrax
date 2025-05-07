import bd
import hashlib

class Vehiculo:
    def __init__(self, idVehiculo=None, placa=None, modelo=None, anio=None, color=None, idTipoVehiculo=None):
        self.idVehiculo = idVehiculo
        self.placa = placa
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.idTipoVehiculo = idTipoVehiculo

    @classmethod
    def obtenerVehiculos(cls):
        try:
            conexion = bd.Conexion()
            listado = conexion.obtener("""
                SELECT
                    idVehiculo,
                    placa,
                    modelo,
                    anio,
                    color,
                    idTipoVehiculo
                FROM vehiculo;
            """)
            return listado
        except Exception as e:
            print(f"Error en obtenerVehiculos: {str(e)}")
            raise
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def obtener_unVehiculo(cls, numplaca):
        try:
            conexion = bd.Conexion()
            vehiculo_encontrado = conexion.obtener("""
                SELECT
                    idVehiculo,
                    placa,
                    modelo,
                    anio,
                    color,
                    idTipoVehiculo
                FROM vehiculo
                WHERE placa = %s;
            """, (numplaca,))
            return vehiculo_encontrado[0] if vehiculo_encontrado else None
        except Exception as e:
            print(f"Error en obtener_unVehiculo: {str(e)}")
            raise
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def insertarVehiculo(cls, placa, modelo, anio, color, idTipoVehiculo):
        try:
            conexion = bd.Conexion()
            # Llamada al SP que devuelve @MSJ y @MSJ2
            conexion.ejecutar(
                "CALL SP_INSERTAR_VEHICULO(%s, %s, %s, %s, %s, @MSJ, @MSJ2);",
                (placa, modelo, anio, color, idTipoVehiculo)
            )
            resultado = conexion.obtener("SELECT @MSJ AS MSJ, @MSJ2 AS MSJ2;")
            return resultado[0]
        except Exception as e:
            print(f"Error en insertarVehiculo: {str(e)}")
            raise
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def actualizarVehiculo(cls, idVehiculo, placa, modelo, anio, color, idTipoVehiculo, estado):
        try:
            conexion = bd.Conexion()
            # Ahora pasamos también 'estado' al SP
            conexion.ejecutar(
                "CALL SP_ACTUALIZAR_VEHICULO(%s, %s, %s, %s, %s, %s, %s, @MSJ, @MSJ2);",
                (idVehiculo, placa, modelo, anio, color, idTipoVehiculo, estado)
            )
            resultado = conexion.obtener("SELECT @MSJ AS MSJ, @MSJ2 AS MSJ2;")
            return resultado[0]
        except Exception as e:
            print(f"Error en actualizarVehiculo: {str(e)}")
            raise
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def darBajaVehiculo(cls, idVehiculo):
        try:
            conexion = bd.Conexion()
            conexion.ejecutar(
                "CALL SP_BAJA_VEHICULO(%s, @MSJ, @MSJ2);",
                (idVehiculo,)
            )
            resultado = conexion.obtener("SELECT @MSJ AS MSJ, @MSJ2 AS MSJ2;")
            return resultado[0]
        except Exception as e:
            print(f"Error en darBajaVehiculo: {str(e)}")
            raise
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def eliminarVehiculo(cls, idVehiculo):
        try:
            conexion = bd.Conexion()
            conexion.ejecutar(
                "CALL SP_ELIMINAR_VEHICULO(%s, @MSJ, @MSJ2);",
                (idVehiculo,)
            )
            resultado = conexion.obtener("SELECT @MSJ AS MSJ, @MSJ2 AS MSJ2;")
            return resultado[0]
        except Exception as e:
            print(f"Error en eliminarVehiculo: {str(e)}")
            raise
        finally:
            if conexion:
                conexion.cerrar()
