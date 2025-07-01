import bd
import string
import random
import os
import xml.etree.ElementTree as ET
from jinja2 import Environment, FileSystemLoader

from Models.tipoDocumento import TipoDocumento
class Pasaje:
    def __init__(self, id, id_detalle_asiento, numero_comprobante, es_pasaje_normal,
                 es_pasaje_libre, es_transferencia, es_reserva, es_cambio_ruta,
                 id_venta, codigo, id_pasaje):
        self.id = id
        self.id_detalle_asiento = id_detalle_asiento
        self.numero_comprobante = numero_comprobante
        self.es_pasaje_normal = es_pasaje_normal
        self.es_pasaje_libre = es_pasaje_libre
        self.es_transferencia = es_transferencia
        self.es_reserva = es_reserva
        self.es_cambio_ruta = es_cambio_ruta
        self.id_venta = id_venta
        self.codigo = codigo
        self.id_pasaje = id_pasaje


    @classmethod
    def obtener_id_por_comprobante(cls, numero_comprobante):
        conexion = None
        try:
            conexion = bd.Conexion()
            sql = "SELECT id FROM pasaje WHERE numeroComprobante = %s;"
            filas = conexion.obtener(sql, (numero_comprobante,))
            return filas[0]['id'] if filas else None
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def obtener_ultimo_comprobante(cls):
        conexion = None
        try:
            conexion = bd.Conexion()
            sql = "SELECT numeroComprobante FROM pasaje ORDER BY id DESC LIMIT 1;"
            filas = conexion.obtener(sql)
            return filas[0]['numeroComprobante'] if filas else None
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def actualizar_id_pasaje_ultimo(cls):
        conexion = None
        try:
            conexion = bd.Conexion()
            # Obtener el último comprobante
            ultimo_comprobante = cls.obtener_ultimo_comprobante()
            if not ultimo_comprobante:
                return {"msj": None, "msj2": "No se encontró comprobante"}
            # Obtener el id correspondiente
            id_pasaje = cls.obtener_id_por_comprobante(ultimo_comprobante)
            if not id_pasaje:
                return {"msj": None, "msj2": "No se encontró pasaje para el comprobante"}
            # Actualizar el campo idPasaje con su propio id
            sql = "UPDATE pasaje SET idPasaje = %s WHERE numeroComprobante = %s;"
            conexion.ejecutar(sql, (id_pasaje, ultimo_comprobante))
            return {"msj": "idPasaje actualizado correctamente", "msj2": None}
        finally:
            if conexion:
                conexion.cerrar()


    @classmethod
    def obtener_todos(cls):
        conexion = None
        try:
            conexion = bd.Conexion()
            return conexion.obtener("""
                SELECT 
                    pas.id,
                    pas.idVenta          AS id_venta,
                    cli.nombre           AS cliente,
                    cli.numero_documento AS num_doc,
                    suc_origen.nombre    AS origen,
                    suc_destino.nombre   AS destino,
                    pas.codigoReserva    AS codigo,
                    pas.esReserva        AS reserva,
                    pas.esPasajeNormal   AS pagado
                FROM pasaje pas
                LEFT JOIN venta v 
                    ON pas.idVenta = v.id
                LEFT JOIN cliente cli 
                    ON v.idCliente = cli.id
                LEFT JOIN detalle_viaje_asiento dvas
                    ON pas.idDetalleViajeAsiento = dvas.id
                LEFT JOIN detalle_viaje dv
                    ON dvas.idDetalle_Viaje = dv.id
                LEFT JOIN sucursal suc_origen 
                    ON dv.idSucursalOrigen = suc_origen.id
                LEFT JOIN sucursal suc_destino 
                    ON dv.idSucursalDestino = suc_destino.id;
            """)
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def obtener_todas_reservas(cls):
        conexion = None
        try:
            conexion = bd.Conexion()
            return conexion.obtener("""
                SELECT
                    pas.id,
                    pas.idVenta          AS id_venta,
                    cli.nombre           AS cliente,
                    cli.numero_documento AS num_doc,
                    suc_origen.nombre    AS origen,
                    suc_destino.nombre   AS destino,
                    pas.codigoReserva    AS codigo,
                    pas.esReserva        AS reserva,
                    pas.esPasajeNormal   AS pagado
                FROM pasaje pas
                LEFT JOIN venta v 
                    ON pas.idVenta = v.id
                LEFT JOIN cliente cli 
                    ON v.idCliente = cli.id
                LEFT JOIN detalle_viaje_asiento dvas
                    ON pas.idDetalleViajeAsiento = dvas.id
                LEFT JOIN detalle_viaje dv
                    ON dvas.idDetalle_Viaje = dv.id
                LEFT JOIN sucursal suc_origen 
                    ON dv.idSucursalOrigen = suc_origen.id
                LEFT JOIN sucursal suc_destino 
                    ON dv.idSucursalDestino = suc_destino.id 
                WHERE pas.esReserva = 1
                AND pas.fecha_reserva >= NOW() - INTERVAL 2 HOUR;
            """)
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def obtener_precio_ruta(cls, num_comprobante, codigo_prom):
        conexion = None
        try:
            conexion = bd.Conexion()
            sql = """SELECT precio FROM pasaje ps WHERE ps.numeroComprobante = %s AND ps.codigo = %s;"""
            return conexion.obtener(sql, (num_comprobante, codigo_prom))
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def detalle_viaje(cls, id_detalle_asiento, idDetalle_Viaje):
        conexion = None
        try:
            conexion = bd.Conexion()
            sql = """SELECT
                            dv.id AS id_detalle_viaje, 
                            dv.fechaSalida, 
                            dv.fechaLlegadaEstimada, 
                            so.nombre AS origen, 
                            sd.nombre AS destino, 
                            so.ciudad AS ciudad_origen, 
                            sd.ciudad AS ciudad_destino,
                            hr.precio + dv.precio AS precio_total,
                            dva.idAsiento as asientoid, dva.idDetalle_Viaje as idViaje
                        FROM 
                            detalle_viaje_asiento dva
                        JOIN 
                            detalle_viaje dv ON dva.idDetalle_Viaje = dv.id
                        JOIN 
                            sucursal so ON dv.idSucursalOrigen = so.id
                        JOIN 
                            sucursal sd ON dv.idSucursalDestino = sd.id
                        JOIN 
                            asiento a ON dva.idAsiento = a.id
                        JOIN 
                            nivel_herramienta nv ON a.id_nivel_herramienta = nv.id
                        JOIN
                            herramienta hr ON nv.id_herramienta = hr.id
                        WHERE 
                            dva.id = %s and dva.idDetalle_Viaje = %s;"""
            return conexion.obtener(sql, (id_detalle_asiento, idDetalle_Viaje))
        finally:
            if conexion:
                conexion.cerrar()


    @classmethod
    def detalle_viaje_general(cls, id_detalle_asiento_list, idDetalle_Viaje):
        conexion = None
        try:
            conexion = bd.Conexion()
            
            # Usamos 'IN' para permitir varios ids de asiento
            sql = """SELECT
                            dv.id AS id_detalle_viaje, 
                            dv.fechaSalida, 
                            dv.fechaLlegadaEstimada, 
                            so.nombre AS origen, 
                            sd.nombre AS destino, 
                            so.ciudad AS ciudad_origen, 
                            sd.ciudad AS ciudad_destino,
                            hr.precio + dv.precio AS precio_total,
                            dva.idAsiento as asientoid, dva.idDetalle_Viaje as idViaje
                        FROM 
                            detalle_viaje_asiento dva
                        JOIN 
                            detalle_viaje dv ON dva.idDetalle_Viaje = dv.id
                        JOIN 
                            sucursal so ON dv.idSucursalOrigen = so.id
                        JOIN 
                            sucursal sd ON dv.idSucursalDestino = sd.id
                        JOIN 
                            asiento a ON dva.idAsiento = a.id
                        JOIN 
                            nivel_herramienta nv ON a.id_nivel_herramienta = nv.id
                        JOIN
                            herramienta hr ON nv.id_herramienta = hr.id
                        WHERE 
                            dva.idAsiento IN (%s) AND dva.idDetalle_Viaje = %s;"""
            
            # Convertir la lista de ids de asientos a una cadena separada por comas
            format_in = ','.join(['%s'] * len(id_detalle_asiento_list))
            
            # Ejecutar la consulta con el array de ids de asiento
            sql = sql % format_in
            return conexion.obtener(sql, tuple(id_detalle_asiento_list) + (idDetalle_Viaje,))
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def cambiarEstadoAsiento(cls, ):
        conexion = None
        try:
            conexion =  bd.Conexion()
            sql = ""
        finally:
            if conexion:
                conexion.cerrar()


    @classmethod
    def dar_baja_cambio_ruta(cls, id_pasaje):
        conexion = None
        try:
            conexion = bd.Conexion()
            conexion.autocommit(False)
            # 1) Verificamos que el pasaje exista y que tenga un cambio de ruta activo
            fila = conexion.obtener(
                "SELECT esCambioRuta FROM pasaje WHERE id = %s FOR UPDATE",
                (id_pasaje,)
            )
            if not fila:
                conexion.rollback()
                return {"msj1": None, "msj2": "Pasaje no encontrado"}
            if fila[0]["esCambioRuta"] != 1:
                conexion.rollback()
                return {"msj1": None, "msj2": "El pasaje no está marcado como cambio de ruta"}

            # 2) Damos de baja el cambio de ruta
            conexion.ejecutar(
                "UPDATE pasaje SET esCambioRuta = 0 WHERE id = %s",
                (id_pasaje,)
            )
            conexion.commit()
            return {"msj1": "Cambio de ruta dado de baja correctamente", "msj2": None}

        except Exception as e:
            if conexion:
                conexion.rollback()
            return {"msj1": None, "msj2": f"Error al dar de baja el cambio de ruta: {e}"}
        finally:
            if conexion:
                conexion.cerrar()


    @classmethod
    def eliminar_cambio_ruta(cls, id_pasaje):
        conexion = None
        try:
            conexion = bd.Conexion()
            conexion.autocommit(False)
            # 1) Verificamos que el pasaje exista y que tenga un cambio de ruta activo
            fila = conexion.obtener(
                "SELECT esCambioRuta FROM pasaje WHERE id = %s FOR UPDATE",
                (id_pasaje,)
            )
            if not fila:
                conexion.rollback()
                return {"msj1": None, "msj2": "Pasaje no encontrado"}
            if fila[0]["esCambioRuta"] != 1:
                conexion.rollback()
                return {"msj1": None, "msj2": "El pasaje no está marcado como cambio de ruta"}

            # 2) Eliminamos físicamente el registro de cambio de ruta
            #    (suponiendo que el pasaje de cambio de ruta es un registro aparte
            #     y se puede eliminar; si no, ajusta la lógica según tu modelo)
            conexion.ejecutar(
                "DELETE FROM pasaje WHERE id = %s AND esCambioRuta = 1",
                (id_pasaje,)
            )
            conexion.commit()
            return {"msj1": "Cambio de ruta eliminado correctamente", "msj2": None}

        except Exception as e:
            if conexion:
                conexion.rollback()
            return {"msj1": None, "msj2": f"Error al eliminar el cambio de ruta: {e}"}
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def obtener_todos_cambiados_ruta(cls):
        conexion = None
        try:
            conexion = bd.Conexion()
            sql = """SELECT
                        p.id                                             AS ID,
                        p.numeroComprobante                              AS NUM_COMPROBANTE,
                        CONCAT(cli.nombre, ' ', cli.ape_paterno, ' ', cli.ape_materno) AS CLIENTE,
                        so.nombre                                        AS ORIGEN,
                        sd.nombre                                        AS DESTINO,
                        v.fecha                                          AS FECHA,
                        p.codigo                                         AS CODIGO,
                        p.precio as PRECIO,
                        dva.idAsiento                                      AS ASIENTO,
                        FROM pasaje p
                        JOIN venta v                    ON v.id = p.idVenta
                        JOIN cliente cli                ON cli.id = v.idCliente
                        JOIN detalle_viaje_asiento dva  ON dva.id = p.idDetalleViajeAsiento
                        JOIN detalle_viaje dv           ON dv.id = dva.idDetalle_Viaje
                        JOIN sucursal so                ON so.id = dv.idSucursalOrigen
                        JOIN sucursal sd                ON sd.id = dv.idSucursalDestino WHERE p.esCambioRuta = 1;"""
            return conexion.obtener(sql)
        finally:
            if conexion:
                conexion.cerrar()

    
    
    @classmethod
    def registrar_cambio_ruta(cls, numero_comprobante, cliente, destino, origen, fecha_viaje, estado, codigo, usuario):
        conexion = None
        try:
            conexion = bd.Conexion()
            conexion.autocommit(False)
            # 1) Buscamos el pasaje por su número de comprobante
            fila = conexion.obtener(
                "SELECT id FROM pasaje WHERE numeroComprobante = %s FOR UPDATE",
                (numero_comprobante,)
            )
            if not fila:
                conexion.rollback()
                return {"msj1": None, "msj2": "Pasaje no encontrado"}

            id_pasaje = fila[0]["id"]

            # 2) Marcamos como cambio de ruta e insertamos los datos relevantes
            conexion.ejecutar(
                """
                UPDATE pasaje
                SET
                  esCambioRuta = 1,
                  codigo = %s,
                  fechaInicioReprogramacion = %s,
                  usuario = %s
                WHERE id = %s
                """,
                (codigo, fecha_viaje, usuario, id_pasaje)
            )

            conexion.commit()
            return {"msj1": "Cambio de ruta registrado correctamente", "msj2": None}

        except Exception as e:
            if conexion:
                conexion.rollback()
            return {"msj1": None, "msj2": f"Error al registrar el cambio de ruta: {e}"}
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def editar_cambio_ruta(cls, numero_comprobante, fecha_viaje, codigo, usuario):
        conexion = None
        try:
            conexion = bd.Conexion()
            conexion.autocommit(False)
            # 1) Bloqueamos el pasaje y verificamos que exista y esté en cambio de ruta
            fila = conexion.obtener(
                "SELECT id, esCambioRuta FROM pasaje WHERE numeroComprobante = %s FOR UPDATE",
                (numero_comprobante,)
            )
            if not fila:
                conexion.rollback()
                return {"msj1": None, "msj2": "Pasaje no encontrado"}
            if fila[0]["esCambioRuta"] != 1:
                conexion.rollback()
                return {"msj1": None, "msj2": "El pasaje no está marcado como cambio de ruta"}

            id_pasaje = fila[0]["id"]

            # 2) Actualizamos los datos del cambio de ruta
            conexion.ejecutar(
                """
                UPDATE pasaje
                   SET fechaInicioReprogramacion = %s,
                       codigo                   = %s,
                       usuario                  = %s
                 WHERE id = %s
                """,
                (fecha_viaje, codigo, usuario, id_pasaje)
            )
            conexion.commit()
            return {"msj1": "Cambio de ruta actualizado correctamente", "msj2": None}

        except Exception as e:
            if conexion:
                conexion.rollback()
            return {"msj1": None, "msj2": f"Error al editar el cambio de ruta: {e}"}
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, id_pasaje):
        conexion = None
        try:
            conexion = bd.Conexion()
            filas = conexion.obtener(
                "SELECT * FROM pasaje WHERE id = %s;", (id_pasaje,)
            )
            return filas[0] if filas else None
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def registrarReserva(cls, id_detalle_asiento, numero_comprobante, id_venta, codigo, id_pasaje=0):
        conexion = None
        try:
            conexion = bd.Conexion()
            # Registro de reserva: solo esReserva=1
            sql = "CALL SP_INSERTAR_PASAJE(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            params = (
                id_detalle_asiento,
                numero_comprobante,
                0,  # esPasajeNormal
                0,  # esPasajeLibre
                0,  # esTransferencia
                1,  # esReserva
                0,  # esCambioRuta
                id_venta,
                codigo,
                id_pasaje,
            )
            conexion.ejecutar(sql, params)
            resultado = conexion.obtener("SELECT @MSJ AS msj, @MSJ2 AS msj2;")
            return resultado[0] if resultado else {"msj": None, "msj2": "Error al recuperar mensaje"}
        except Exception as e:
            return {"msj": None, "msj2": f"Error en la reserva: {e}"}
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def esCambioRuta(cls, numero_comprobante):
        conexion = None
        try:
            conexion = bd.Conexion()
            sql = "UPDATE pasaje SET esCambioRuta = 1, esReserva = 0, esPasajeNormal = 0, esPasajeLibre = 0, esTransferencia = 0 WHERE numeroComprobante = %s;"
            conexion.ejecutar(sql, (numero_comprobante,))
            sql = """UPDATE detalle_viaje_asiento dva
                        INNER JOIN pasaje p
                        ON p.idDetalleViajeAsiento = dva.id
                        SET dva.esDisponible = 1
                        WHERE p.numeroComprobante = %s; 
                """
            conexion.ejecutar(sql, (numero_comprobante,))
            resultado = conexion.obtener("SELECT esCambioRuta FROM pasaje WHERE numeroComprobante = %s;", (numero_comprobante,))
            if resultado:
                return resultado[0]['esCambioRuta'] == 1
            return False
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def modificarReserva(cls, id_pasaje, id_detalle_asiento, numero_comprobante,
                         es_pasaje_normal, es_pasaje_libre, es_transferencia,
                         es_reserva, es_cambio_ruta, id_venta, codigo, id_pasaje_padre=0):
        conexion = None
        try:
            conexion = bd.Conexion()
            sql = "CALL SP_MODIFICAR_PASAJE(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            params = (
                id_pasaje,
                id_detalle_asiento,
                numero_comprobante,
                es_pasaje_normal,
                es_pasaje_libre,
                es_transferencia,
                es_reserva,
                es_cambio_ruta,
                id_venta,
                codigo,
                id_pasaje_padre,
            )
            conexion.ejecutar(sql, params)
            resultado = conexion.obtener("SELECT @MSJ AS msj, @MSJ2 AS msj2;")
            return resultado[0] if resultado else {"msj": None, "msj2": "Error al recuperar mensaje"}
        except Exception as e:
            return {"msj": None, "msj2": f"Error al modificar pasaje: {e}"}
        finally:
            if conexion:
                conexion.cerrar()
                
    @classmethod
    def generar_codigo_unico(cls, length=8):
        alphabet = string.ascii_uppercase + string.digits
        conexion = bd.Conexion()
        print(9)
        try:
            while True:
                code = ''.join(random.choices(alphabet, k=length))
                resultado = conexion.obtener(
                    "SELECT 1 FROM pasaje WHERE codigo = %s LIMIT 1",
                    (code,)
                )
                if not resultado:
                    return code
            print(10)
        finally:
            conexion.cerrar()
            # Si existe, se itera de nuevo
            # Se esta considerando 26 caracteres alfabéticos y 10 dígitos, lo que da un total de 36 caracteres por 8 posiciones,
            # lo que da un total de 2,821,109,907,456 combinaciones posibles.
    
    @classmethod
    def generar_codigo_reserva(cls):
        conexion = bd.Conexion()
        try:
            while True:
                codigo = f"RES-{''.join(random.choices(string.ascii_uppercase, k=5))}-{random.randint(1000, 9999)}"
                fila = conexion.obtener(
                    "SELECT codigo FROM pasaje WHERE codigo = %s LIMIT 1",
                    (codigo,)
                )
                if not fila:
                    return codigo
        finally:
            conexion.cerrar()
            # Genera un código de reserva único con el formato "RES-XXXXX-YYYY"
            # donde XXXXX es una cadena aleatoria de 5 letras y YYYY es un número entre 1000 y 9999.
            # lo que da un total de 11,881,376,000 combinaciones posibles.
    
    @classmethod
    def cambiar_estado_transaccion(cls, id_pasaje):
        conexion = bd.Conexion()
        try:
            sql_select = "SELECT enTransaccion FROM pasaje WHERE id = %s;"
            filas = conexion.obtener(sql_select, (id_pasaje,))
            if not filas:
                return {"error": "Pasaje no encontrado"}

            estado_actual = filas[0]['enTransaccion']
            nuevo_estado = 0 if estado_actual else 1

            sql_update = "UPDATE pasaje SET enTransaccion = %s WHERE id = %s;"
            conexion.ejecutar(sql_update, (nuevo_estado, id_pasaje))

            return {"nuevoEstado": nuevo_estado}
        except Exception as e:
            raise
        finally:
            conexion.cerrar()

    @classmethod
    def generar_numComprobante(cls):
        conexion = bd.Conexion()
        try:
            row = conexion.obtener("SELECT MAX(numeroComprobante) as numero FROM pasaje")
            ultimo = row[0] if row and row[0] else None
            if not ultimo['numero']:
                return 'A000-00000001'
            ultimo = ultimo['numero']
            letra = ultimo[0]
            serie = int(ultimo[1:4])
            corr  = int(ultimo[5:]) + 1
            if corr > 99999999:
                corr = 0
                serie += 1

                if serie > 999:
                    serie = 0
                    if letra.upper() == 'Z':
                        raise ValueError("Se alcanzó el límite máximo: Z999-99999999")
                    letra = chr(ord(letra.upper()) + 1)

            s_txt = f"{serie:03d}"
            c_txt = f"{corr:08d}"
            return f"{letra}{s_txt}-{c_txt}"

        finally:
            conexion.cerrar()

    
    @classmethod
    def obtenerDatosPasaje(cls, numComprobante):
        conexion = None
        try:
            conexion = bd.Conexion()
            query = """
            SELECT 
                td.abreviatura AS tipo_documento,
                pa.numero_documento,
                CONCAT_WS(' ', pa.nombre, pa.ape_paterno, pa.ape_materno) AS nombre_completo,
                s_origen.id AS idSucursalOrigen,
                s_origen.ciudad AS origen,
                s_destino.id AS idSucursalDestino,
                s_destino.ciudad AS destino,
                dv.fechaSalida AS fecha_salida,
                DATE_FORMAT(dv.fechaSalida, '%%H:%%i') AS hora_salida,
                a.nombre AS asiento,
                ser.nombre AS servicio,
                pas.codigo AS codigo_pasaje,
                pas.enTransaccion AS estado_transaccion,
                v.idEstadoViaje AS estado_viaje,    
                pas.numeroComprobante,
                pas.idDetalleViajeAsiento,
                pas.id, pa.email as email_pasajero
            FROM pasaje pas 
            INNER JOIN detalle_viaje_asiento dva 
                ON dva.id = pas.idDetalleViajeAsiento
            INNER JOIN detalle_viaje dv 
                ON dv.id = dva.idDetalle_Viaje
            INNER JOIN detalle_pasaje dp 
                ON dp.idPasaje = pas.id 
            INNER JOIN pasajero pa 
                ON pa.id = dp.idPasajero
            INNER JOIN tipo_documento td 
                ON td.id = pa.idTipoDocumento
            INNER JOIN asiento a 
                ON a.id = dva.idAsiento
            INNER JOIN sucursal s_origen 
                ON s_origen.id = dv.idSucursalOrigen
            INNER JOIN sucursal s_destino 
                ON s_destino.id = dv.idSucursalDestino
            INNER JOIN vehiculo ve 
                ON ve.id = a.id_vehiculo
            INNER JOIN tipo_vehiculo tv 
                ON tv.id = ve.id_tipo_vehiculo
            INNER JOIN servicio ser 
                ON ser.id = tv.id_servicio
            INNER JOIN viaje v 
                ON v.id = dv.idViaje
            WHERE dp.viajeEnBrazos != 1
              AND pas.numeroComprobante = %s;
        """
            filas = conexion.obtener(query, (numComprobante,))
            return filas[0] if filas else None
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def eliminarReserva(cls, id_pasaje):
        conexion = None
        try:
            conexion = bd.Conexion()
            conexion.ejecutar("CALL SP_ELIMINAR_PASAJE(%s);", (id_pasaje,))
            resultado = conexion.obtener("SELECT @MSJ AS msj, @MSJ2 AS msj2;")
            return resultado[0] if resultado else {"msj": None, "msj2": "Error al recuperar mensaje"}
        except Exception as e:
            return {"msj": None, "msj2": f"Error al eliminar pasaje: {e}"}
        finally:
            if conexion:
                conexion.cerrar()
                
    @classmethod
    def obtener_estados_pasaje(cls, id_pasaje):
        conexion = None
        try:
            conexion = bd.Conexion()
            sql = """
                SELECT 
                    esTransferencia AS esTransferencia,
                    esReembolso AS esReembolso,
                    esCambioRuta AS esCambioRuta,
                    esPasajeLibre AS esPasajeLibre
                FROM pasaje
                WHERE id = %s AND enTransaccion = 1;
            """
            resultado = conexion.obtener(sql, (id_pasaje,))[0]
            if resultado['esTransferencia'] == 1:
                resultado['estado'] = 'Ya se ha realizado una transferencia de este pasaje.'
            elif resultado['esReembolso'] == 1:
                resultado['estado'] = 'Ya se ha realizado un reembolso de este pasaje.'
            elif resultado['esCambioRuta'] == 1:
                resultado['estado'] = 'Ya se ha realizado un cambio de ruta de este pasaje.'
            elif resultado['esPasajeLibre'] == 1:
                resultado['estado'] = 'Ya se ha convertido a pasaje libre este pasaje.'
            else:
                resultado['estado'] = 'El pasaje se encuentra en un proceso de transacción.'
            return resultado
        
        finally:
            if conexion:
                conexion.cerrar()
    
    @classmethod
    def convertirPasajeLibre(cls, id_pasaje, idDetViajeAs):
        conexion = None
        try:
            conexion = bd.Conexion()
            
            sql_update = """
                UPDATE pasaje
                SET esPasajeLibre = 1,
                    enTransaccion = 1,
                    esPasajeNormal = 0,
                    esReserva = 0
                WHERE id = %s;
            """
            conexion.ejecutar(sql_update, (id_pasaje,), auto_commit=False)
            
            sql_update2 = """
                UPDATE detalle_viaje_asiento
                SET esDisponible = 1
                WHERE id = %s;
            """
            conexion.ejecutar(sql_update2, (idDetViajeAs,), auto_commit=False)

            conexion.conn.commit()
            
            return {"msj": "Pasaje convertido a libre exitosamente", "msj2": None}
        except Exception as e:
            conexion.conn.rollback()
            return {"msj": None, "msj2": f"Error al convertir pasaje a libre: {e}"}
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def realizarTransferencia(cls, pasaje: dict, persona1: dict, persona2: dict = None):
        conexion = None
        try:
            conexion = bd.Conexion()
            # 1) Marcar el pasaje original como transferencia
            sql_update = """
                UPDATE pasaje
                SET esTransferencia = 1,
                    esReserva = 0,
                    enTransaccion   = 1
                WHERE id = %s;
            """
            conexion.ejecutar(sql_update, (pasaje['id'],), auto_commit=False)

            # 2) Generar comprobante y código
            num_comp  = cls.generar_numComprobante()
            cod_unico = cls.generar_codigo_unico()

            # 4) Insertar nuevo pasaje (transferencia)
            sql_insert = """
                INSERT INTO pasaje (
                    idDetalleViajeAsiento,
                    numeroComprobante,
                    esPasajeNormal,
                    idVenta,
                    codigo,
                    idPasaje
                ) VALUES (%s, %s, %s, %s, %s, %s);
            """
            params_insert = (
                pasaje['idDetalleViajeAsiento'],
                num_comp,
                1,          # esPasajeNormal
                1,          # idVenta (ajustar según tu lógica)
                cod_unico,
                pasaje['id']   # referencia al pasaje original
            )
            conexion.ejecutar(sql_insert, params_insert, auto_commit=False)

            # 5) Capturar el nuevo ID generado
            id_nuevo_pasaje = conexion.obtener(
                "SELECT LAST_INSERT_ID() AS id;"
            )[0]['id']

            # 6) Helpers para pasajero y detalle_pasaje
            def insertar_pasajero(p):
                sql = """
                    INSERT INTO pasajero (
                        nombre, ape_paterno, ape_materno,
                        idTipoDocumento, numero_documento,
                        sexo, f_nacimiento, telefono, email
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
                """
                
                params = (
                    p.get('nombre', ''),
                    p.get('ape_paterno', ''),
                    p.get('ape_materno', ''),
                    TipoDocumento.obtener_por_nombre(p.get('nombreDocumento')),
                    p.get('numero_documento', ''),
                    p.get('sexo'),
                    p.get('f_nacimiento'),
                    p.get('telefono', ''),
                    p.get('email', '')
                )
                conexion.ejecutar(sql, params, auto_commit=False)
                return conexion.obtener("SELECT LAST_INSERT_ID() AS id;")[0]['id']

            def insertar_detalle(id_pas, p):
                sql = """
                    INSERT INTO detalle_pasaje (
                        idPasajero, idPasaje, esMenorEdad, viajeEnBrazos, fecha_registro
                    ) VALUES (%s, %s, %s, %s, NOW());
                """
                params = (
                    id_pas,
                    id_nuevo_pasaje,
                    p.get('esMenorEdad'),
                    p.get('viajeEnBrazos')
                )
                conexion.ejecutar(sql, params, auto_commit=False)

            # 7) Ejecutar inserciones para persona1 y persona2
            id_p1 = insertar_pasajero(persona1)
            insertar_detalle(id_p1, persona1)

            if persona2 and persona2.get('nombre'):
                id_p2 = insertar_pasajero(persona2)
                insertar_detalle(id_p2, persona2)

            # 8) Commit y retorno
            conexion.conn.commit()
            return {"msj": "Transferencia realizada con éxito", "msj2": None}

        except Exception as e:
            conexion.conn.rollback()
            return {"msj": None, "msj2": f"Error al realizar transferencia: {e}"}
        finally:
            if conexion:
                conexion.cerrar()

        
    @classmethod
    def pagarReserva(cls, id_pasaje):
        conexion = None
        try:
            conexion = bd.Conexion()
            # Llama al SP con la variable de salida en @MSJ y @MSJ2
            conexion.ejecutar(
                "CALL SP_CAMBIAR_ESTADO_PASAJE(%s, @MSJ, @MSJ2);",
                (id_pasaje,)
            )
            # Recupera los mensajes de salida
            resultado = conexion.obtener(
                "SELECT @MSJ AS msj, @MSJ2 AS msj2;"
            )
            return resultado[0] if resultado else {"msj": None, "msj2": "Error al recuperar mensajes"}
        except Exception as e:
            return {"msj": None, "msj2": f"Error al cambiar estado de pasaje: {e}"}
        finally:
            if conexion:
                conexion.cerrar()
    
    @classmethod
    def generar_xml_comprobante(cls, datos):
        comprobante = ET.Element('comprobante')

        ET.SubElement(comprobante, 'ruc').text = datos['ruc']
        
        cliente = ET.SubElement(comprobante, 'cliente')
        ET.SubElement(cliente, 'nombre').text = datos['nombre_completo']
        ET.SubElement(cliente, 'tipo_documento').text = datos['tipo_documento']
        ET.SubElement(cliente, 'numero_documento').text = datos['numero_documento']

        servicio = ET.SubElement(comprobante, 'servicio')
        ET.SubElement(servicio, 'origen').text = datos['origen']
        ET.SubElement(servicio, 'destino').text = datos['destino']
        ET.SubElement(servicio, 'fecha_salida').text = datos['fecha_salida']
        ET.SubElement(servicio, 'hora_salida').text = datos['hora_salida']
        ET.SubElement(servicio, 'asiento').text = datos['asiento']
        ET.SubElement(servicio, 'codigo_pasaje').text = datos['codigo_pasaje']
        # ET.SubElement(comprobante, 'importe').text = datos['importe']

        tree = ET.ElementTree(comprobante)
        carpeta = os.path.join('Static', 'xml')
        os.makedirs(carpeta, exist_ok=True)
        
        nombre_archivo = f"{datos['numeroComprobante'].replace('/', '-')}.xml"
        ruta_archivo = os.path.join(carpeta, nombre_archivo)

        tree.write(ruta_archivo, encoding='utf-8', xml_declaration=True)
        return ruta_archivo 
    
    @classmethod
    def obtener_ultima_venta(cls):
        conexion = None
        try:
            conexion = bd.Conexion()
            conexion.ejecutar("SELECT MAX(id) FROM pasaje;")
            resultado = conexion.obtener()
            return resultado[0] if resultado and resultado[0] else 0
        finally:
            if conexion:
                conexion.cerrar()
                
    @classmethod
    def obtener_numComprobante_venta(cls, id_venta):
        conexion = None
        try:
            conexion = bd.Conexion()
            filas = conexion.obtener("SELECT numeroComprobante FROM pasaje WHERE id_venta = %s;", (id_venta,))
            return filas[0] if filas else None
        finally:
            if conexion:
                conexion.cerrar()
    
    @classmethod         
    def generar_pdf_desde_xml(cls, ruta_xml):
        tree = ET.parse(ruta_xml)
        root = tree.getroot()

        datos = {
            'ruc': root.findtext('ruc'),
            'cliente_nombre': root.findtext('cliente/nombre'),
            'cliente_dni': root.findtext('cliente/dni'),
            'ruta': root.findtext('servicio/ruta'),
            'fecha': root.findtext('servicio/fecha'),
            'hora': root.findtext('servicio/hora'),
            'asiento': root.findtext('servicio/asiento'),
            'importe': root.findtext('importe')
        }

        env = Environment(loader=FileSystemLoader('Views/Ecommerce/home'))
        template = env.get_template('comprobante_template.html')
        html_renderizado = template.render(datos)

        nombre_archivo = os.path.splitext(os.path.basename(ruta_xml))[0] + ".pdf"
        ruta_pdf = os.path.join('Static', 'pdf', nombre_archivo)
        os.makedirs(os.path.dirname(ruta_pdf), exist_ok=True)

        # HTML(string=html_renderizado).write_pdf(ruta_pdf)
        return ruta_pdf
    
    @classmethod
    def obtener_id_por_numComprobante(cls, numcomprobante):
        conexion = None
        try:
            conexion = bd.Conexion()
            filas = conexion.obtener(
                "SELECT id FROM pasaje where numeroComprobante= %s;", (numcomprobante,)
            )
            return filas[0] if filas else None
        finally:
            if conexion:
                conexion.cerrar()
    
    @classmethod
    def validar_solicitud_reembolso(cls, numcomprobante):
        conexion = None
        try:
            conexion = bd.Conexion()
            filas = conexion.obtener(
                "SELECT * FROM pasaje pa inner join reembolso re on re.idPasaje=pa.id where pa.numeroComprobante= %s;", (numcomprobante,)
            )
            return filas[0] if filas else None
        finally:
            if conexion:
                conexion.cerrar()
                
    @classmethod
    def validar_codigo_reprogramacion(cls, codigo):
        conexion = None
        try:
            conexion = bd.Conexion()
            filas = conexion.obtener(
                "SELECT * FROM `pasaje` WHERE codigo= %s and fechaInicioReprogramacion is not null and fechaFinReprogramacion is not null", (codigo,)
            )
            return filas[0] if filas else None
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def liberarAsientosxReserva(cls):
        conexion = None
        try:
            conexion = bd.Conexion()
            ids = conexion.obtener("""
                SELECT pas.id as idPasaje, pas.idDetalleViajeAsiento as id
                FROM pasaje pas
                JOIN detalle_viaje_asiento dva ON dva.id = pas.idDetalleViajeAsiento
                WHERE pas.esReserva = 1
                AND pas.fecha_reserva IS NOT NULL
                AND pas.fecha_reserva < NOW() - INTERVAL 2 HOUR
                AND dva.esDisponible = 0
                AND pas.reservaLiberada = 0
                AND NOT EXISTS (
                    SELECT 1
                    FROM pasaje p2
                    WHERE p2.idDetalleViajeAsiento = pas.idDetalleViajeAsiento
                    AND p2.esReserva = 0
                );
            """)

            if ids:
                print('Ids', ids)
                for idReserva in ids:
                    conexion.ejecutar("UPDATE pasaje SET reservaLiberada = 1 WHERE id = %s", (idReserva['idPasaje'],), auto_commit=False)
                    
                    sentencia = "UPDATE detalle_viaje_asiento SET esDisponible=1 WHERE id="+str(idReserva['id'])
                    conexion.ejecutar(sentencia, auto_commit=False)

                conexion.conn.commit()
                
        except Exception as e:
            conexion.conn.rollback()
            print("Ha ocurrido un error: "+repr(e))
        finally:
            if conexion != None:
                conexion.cerrar()
