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
                    v.id as id,
                    v.placa as placa,
                    v.anio as anio,
                    v.color as color,
                    tpve.nombre as tipoVehiculo,
                    m.nombre as marca,
                    v.estado as estado
                FROM vehiculo v left join tipo_vehiculo tpve on v.id_tipo_vehiculo=tpve.id inner join marca m on tpve.id_marca=m.id;
            """)
            return listado
        except Exception as e:
            print(f"Error en obtenerVehiculos: {str(e)}")
            raise
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def obtener_unVehiculo(cls, idVehiculo):
        try:
            conexion = bd.Conexion()
            listado = conexion.obtener("""SELECT * FROM vehiculo WHERE id = %s;""", (idVehiculo,))

            return listado[0] if listado else None
        except Exception as e:
            print(f"Error en obtener_unVehiculo: {str(e)}")
            raise
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def insertarVehiculo(cls, placa, anio, color, idTipoVehiculo):
        try:
            conexion = bd.Conexion()
            # Llamada al SP que devuelve @MSJ y @MSJ2
            conexion.ejecutar(
                "CALL SP_INSERTAR_VEHICULO(%s, %s, %s, %s);",
                (placa, anio, color, idTipoVehiculo)
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
    def actualizarVehiculo(cls, idVehiculo, placa, anio, color, idTipoVehiculo, estado):
        try:
            conexion = bd.Conexion()
            # Ahora pasamos también 'estado' al SP
            conexion.ejecutar(
                "CALL SP_ACTUALIZAR_VEHICULO(%s, %s, %s, %s, %s, %s);",
                (idVehiculo, placa, anio, color, idTipoVehiculo, estado)
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
                "CALL SP_BAJA_VEHICULO(%s);",
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
                "CALL SP_ELIMINAR_VEHICULO(%s);",
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
