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
                    tpve.id as idTipoVehiculo,
                    tpve.nombre as tipoVehiculo,
                    s.id as idServicio,
                    s.nombre as servicio,
                    m.nombre as marca,
                    v.estado as estado
                FROM vehiculo v left join tipo_vehiculo tpve on v.id_tipo_vehiculo=tpve.id inner join marca m on tpve.id_marca=m.id inner join servicio s on tpve.id_servicio = s.id;
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
    def insertarVehiculo(cls, placa, anio, color, idTipoVehiculo, estado, usuario):
        conexion = bd.Conexion()
        try:
            conexion.conn.begin()
            # 1) Crear vehículo
            cursor = conexion.ejecutar(
                "INSERT INTO vehiculo(placa, anio, color, id_tipo_vehiculo, estado, usuario) "
                "VALUES (%s, %s, %s, %s, %s, %s)",
                (placa, anio, color, idTipoVehiculo, estado, usuario),
                auto_commit=False
            )
            idVehiculo = cursor.lastrowid

            # 2) Generar asientos según diseño de tipo_vehiculo
            cursor = conexion.ejecutar(
                """
                SELECT nh.id AS id, nh.x_dimension AS x, nh.y_dimension AS y
                FROM tipo_vehiculo tv
                INNER JOIN nivel n ON tv.id = n.id_tipo_vehiculo
                INNER JOIN nivel_herramienta nh ON nh.id_nivel = n.id
                INNER JOIN herramienta h ON nh.id_herramienta = h.id
                WHERE h.id_tipo = 1 and tv.id = %s
                """,
                (idTipoVehiculo,),
                auto_commit=False
            )
            lista_codigos = cursor.fetchall()
            for codigo in lista_codigos:
                id_nh = codigo['id']
                fila = codigo['x']
                columna = int(codigo['y'])

                letra = chr(64+columna)
                nombre = f"{letra}{fila}"
                cursor = conexion.ejecutar("INSERT INTO asiento (nombre,id_vehiculo,id_nivel_herramienta,estado,usuario) VALUES (%s,%s,%s,%s,%s)",(nombre,idVehiculo,id_nh,1,usuario),auto_commit=False)

            conexion.conn.commit()
            return True
        except Exception as e:
            conexion.conn.rollback()
            print(f"Error en insertarVehiculo: {e}")
            return False
        finally:
            conexion.cerrar()


    @classmethod
    def actualizarVehiculo(cls, idVehiculo, placa, anio, color, idTipoVehiculo, estado, usuario):
        conexion = bd.Conexion()
        try:
            conexion.conn.begin()

            # 1) Verificar que este vehículo NO esté en ningún viaje activo
            existe_en_viaje = conexion.obtener(
                "SELECT 1 FROM viaje vi WHERE vi.idVehiculo = %s LIMIT 1",
                (idVehiculo,)
            )
            if existe_en_viaje:
                raise Exception("No se puede modificar: el vehículo está asignado a un viaje.")

            # 2) Actualizar datos básicos del vehículo
            conexion.ejecutar(
                """
                UPDATE vehiculo
                   SET placa            = %s,
                       anio             = %s,
                       color            = %s,
                       id_tipo_vehiculo = %s,
                       estado           = %s
                 WHERE id = %s
                """,
                (placa, anio, color, idTipoVehiculo, estado, idVehiculo),
                auto_commit=False
            )

            # 3) Regenerar asientos: primero eliminar los viejos
            conexion.ejecutar(
                "DELETE FROM asiento WHERE id_vehiculo = %s",
                (idVehiculo,),
                auto_commit=False
            )

            # 4) Volver a insertar asientos según el nuevo tipo_vehiculo
            cursor = conexion.ejecutar(
                """
                SELECT nh.id AS id, nh.x_dimension AS x, nh.y_dimension AS y
                FROM tipo_vehiculo tv
                INNER JOIN nivel n ON tv.id = n.id_tipo_vehiculo
                INNER JOIN nivel_herramienta nh ON nh.id_nivel = n.id
                INNER JOIN herramienta h ON nh.id_herramienta = h.id
                WHERE h.id_tipo = 1 and tv.id = %s
                """,
                (idTipoVehiculo,),
                auto_commit=False
            )
            lista_codigos = cursor.fetchall()
            for codigo in lista_codigos:
                id_nh = codigo['id']
                fila = codigo['x']
                columna = int(codigo['y'])

                letra = chr(64+columna)
                nombre = f"{letra}{fila}"
                cursor = conexion.ejecutar("INSERT INTO asiento (nombre,id_vehiculo,id_nivel_herramienta,estado,usuario) VALUES (%s,%s,%s,%s,%s)",(nombre,idVehiculo,id_nh,1,usuario),auto_commit=False)


            conexion.conn.commit()
            return {"MSJ": "Vehículo y asientos actualizados correctamente", "MSJ2": ""}
        except Exception as e:
            conexion.conn.rollback()
            return {"MSJ": "", "MSJ2": f"Error al actualizar vehículo: {e}"}
        finally:
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
