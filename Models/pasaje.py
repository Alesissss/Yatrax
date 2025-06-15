import bd
import string
import random

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
                    pas.codigo,
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
        try:
            while True:
                code = ''.join(random.choices(alphabet, k=length))
                conexion.ejecutar(
                    "SELECT 1 FROM pasaje WHERE codigo = %s LIMIT 1",
                    (code,)
                )
                if not conexion.obtener():
                    return code
        finally:
            conexion.cerrar()
            # Si existe, se itera de nuevo
            # Se esta considerando 26 caracteres alfabéticos y 10 dígitos, lo que da un total de 36 caracteres por 8 posiciones,
            # lo que da un total de 2,821,109,907,456 combinaciones posibles.
    
    @classmethod
    def generar_numComprobante(cls):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("SELECT MAX(numeroComprobante) FROM pasaje")
            row = conexion.obtener()
            ultimo = row[0] if row and row[0] else None

            if not ultimo:
                return 'A000-00000001'

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
                    s_origen.ciudad AS origen,
                    s_destino.ciudad AS destino,
                    dv.fechaSalida AS fecha_salida,
                    DATE_FORMAT(dv.fechaSalida, '%%H:%%i') AS hora_salida,
                    a.nombre AS asiento,
                    ser.nombre AS servicio
                        FROM pasaje pas 
                        INNER JOIN detalle_viaje_asiento dva ON dva.id = pas.idDetalleViajeAsiento
                        INNER JOIN detalle_viaje dv ON dv.id = dva.idDetalle_Viaje
                        INNER JOIN detalle_pasaje dp ON dp.idPasaje = pas.id 
                        INNER JOIN pasajero pa ON pa.id = dp.id
                        INNER JOIN tipo_documento td ON td.id = pa.idTipoDocumento
                        INNER JOIN asiento a ON a.id = dva.idAsiento
                        INNER JOIN sucursal s_origen ON s_origen.id = dv.idSucursalOrigen
                        INNER JOIN sucursal s_destino ON s_destino.id = dv.idSucursalDestino
                        INNER JOIN vehiculo ve ON ve.id = a.id_vehiculo
                        INNER JOIN tipo_vehiculo tv ON tv.id = ve.id_tipo_vehiculo
                        INNER JOIN servicio ser ON ser.id = tv.id_servicio
                        WHERE dp.viajeEnBrazos != 0 AND pas.numeroComprobante=%s;
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