from datetime import datetime
from Models.tipoDocumento import TipoDocumento
from Models.tipoComprobante import TipoComprobante
from Models.promocion import Promocion
from Models.pasaje import Pasaje
from Models.cliente import Cliente
import bd  # Tu clase de conexión

class Reserva:

    @classmethod
    def registrar_operacion(cls, contacto: dict, pago: dict, ventas: dict,
                            codigoReserva: str, fecha_reserva: datetime):
        conexion = bd.Conexion()
        try:
            conexion.conn.begin()

            # 1. CLIENTE: buscar por documento o insertar
            cliente_data = Cliente.obtener_id_por_numero_documento(
                contacto.get("numero_documento") or contacto.get("ruc")
            )
            if cliente_data:
                id_cliente = cliente_data["id"]
            else:
                # Insertar nuevo cliente según tipo de comprobante
                if contacto.get("tipo_comprobante") == "1":  # Boleta
                    sql_cli = """
                        INSERT INTO cliente
                          (nombre, ape_paterno, ape_materno,
                           numero_documento, id_tipo_doc,
                           telefono, email)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """
                    params_cli = (
                        contacto.get("nombres"),
                        contacto.get("apellido_paterno"),
                        contacto.get("apellido_materno"),
                        contacto.get("numero_documento"),
                        TipoDocumento.obtener_por_nombre(contacto.get("tipo_documento")),
                        contacto.get("telefono"),
                        contacto.get("email")
                    )
                else:  # Factura
                    sql_cli = """
                        INSERT INTO cliente
                          (nombre, numero_documento, tipoDocumento,
                           telefono, email, direccion)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """
                    params_cli = (
                        contacto.get("razon_social"),
                        contacto.get("ruc"),
                        TipoDocumento.obtener_por_nombre(contacto.get("tipo_documento")),
                        contacto.get("telefono"),
                        contacto.get("email"),
                        contacto.get("direccion")
                    )
                conexion.ejecutar(sql_cli, params_cli, auto_commit=False)
                id_cliente = conexion.cursor.lastrowid

            # 2. VENTA (reserva): calcular totales
            # sumamos todos los precios de los asientos
            total_bruto = sum(float(p.get("precio", 0)) for p in ventas.values())
            igv_rate   = pago.get("igv", 0.0)
            subtotal   = total_bruto / (1 + igv_rate) if igv_rate else total_bruto
            igv_val    = total_bruto - subtotal

            # si hay cupón, obtener idPromocion
            cod_promo = None
            datos_esp = pago.get("datos_especificos", {})
            if datos_esp.get("codigo_promocional"):
                prom = Promocion.obtener_por_codigo(datos_esp["codigo_promocional"])
                cod_promo = prom if prom else None

            # insert en venta
            if cod_promo:
                sql_vta = """
                    INSERT INTO venta
                      (idCliente, fecha, subTotal, igv,
                       idMetodoPago, idTipoComprobante, idPromocion)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                params_vta = (
                    id_cliente,
                    fecha_reserva,
                    subtotal,
                    igv_val,
                    pago.get("metodo_especifico"),
                    contacto.get("tipo_comprobante"),
                    cod_promo
                )
            else:
                sql_vta = """
                    INSERT INTO venta
                      (idCliente, fecha, subTotal, igv,
                       idMetodoPago, idTipoComprobante)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                params_vta = (
                    id_cliente,
                    fecha_reserva,
                    subtotal,
                    igv_val,
                    pago.get("metodo_especifico"),
                    contacto.get("tipo_comprobante")
                )
            conexion.ejecutar(sql_vta, params_vta, auto_commit=False)
            id_venta = conexion.cursor.lastrowid

            # 3. PASAJERO, PASAJE y DETALLE_PASAJE para cada asiento
            for asiento_id, pas in ventas.items():
                # pasajero
                sql_pasj = """
                    INSERT INTO pasajero
                      (nombre, ape_paterno, ape_materno,
                       numero_documento, idTipoDocumento,
                       sexo, f_nacimiento, telefono, email)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                params_pasj = (
                    pas.get("nombres"),
                    pas.get("apellidoPaterno"),
                    pas.get("apellidoMaterno"),
                    pas.get("numDoc"),
                    TipoDocumento.obtener_por_nombre(pas.get("tipoDoc")),
                    pas.get("sexo"),
                    pas.get("fechaNacimiento"),
                    pas.get("telefono"),
                    pas.get("correo")
                )
                conexion.ejecutar(sql_pasj, params_pasj, auto_commit=False)
                id_pasajero = conexion.cursor.lastrowid

                # pasaje (reserva)
                num_comp   = Pasaje.generar_numComprobante()
                cod_unico  = Pasaje.generar_codigo_unico()
                precio     = float(pas.get("precio", 0))
                sql_pj = """
                    INSERT INTO pasaje
                      (idDetalleViajeAsiento, numeroComprobante,
                       esPasajeNormal, esPasajeLibre, esTransferencia,
                       esReserva, esCambioRuta,
                       idVenta, codigo, enTransaccion,
                       codigoReserva, fecha_reserva, precio)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                params_pj = (
                    asiento_id,
                    None,
                    0, 0, 0,
                    1, 0,       # esReserva=1
                    id_venta,
                    cod_unico,
                    0,
                    codigoReserva,
                    fecha_reserva,
                    precio
                )
                conexion.ejecutar(sql_pj, params_pj, auto_commit=False)
                id_pasaje = conexion.cursor.lastrowid

                # detalle_pasaje
                sql_det = """
                    INSERT INTO detalle_pasaje
                      (idPasajero, idPasaje, esMenorEdad, viajeEnBrazos, fecha_registro)
                    VALUES (%s, %s, %s, %s, %s)
                """
                params_det = (
                    id_pasajero,
                    id_pasaje,
                    int(pas.get("esMenor", False)),
                    int(pas.get("brazos", False)),
                    datetime.now()
                )
                conexion.ejecutar(sql_det, params_det, auto_commit=False)

            # 4. Confirmar todo
            conexion.conn.commit()
            return {
                "status": 1,
                "msg": "Reserva registrada correctamente",
                "id_reserva": id_venta
            }

        except Exception as e:
            conexion.conn.rollback()
            return {
                "status": -1,
                "msg": f"Error al registrar reserva: {e}"
            }

        finally:
            conexion.cerrar()
