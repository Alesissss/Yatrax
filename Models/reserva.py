from datetime import datetime
from Models.tipoDocumento import TipoDocumento
from Models.promocion import Promocion
from Models.pasaje import Pasaje
import bd  # Utilizamos tu clase Conexion personalizada

class Reserva:

    @classmethod
    def registrar_operacion(cls, contacto: dict, pago: dict, ventas: dict,codigoReserva,fecha):
        conexion = bd.Conexion()
        try:
            # 1. Registrar CLIENTE
            if(contacto.get("tipo_comprobante") == "1"):  # BOLETA
                insert_cliente = """
                    INSERT INTO cliente (nombre, ape_paterno, ape_materno, numero_documento, id_tipo_doc, telefono, email)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                conexion.ejecutar(insert_cliente, (
                    contacto.get("nombres"),
                    contacto.get("apellido_paterno"),
                    contacto.get("apellido_materno"),
                    contacto.get("numero_documento"),
                    TipoDocumento.obtener_por_nombre(contacto.get("tipo_documento")),
                    contacto.get("telefono"),
                    contacto.get("email")
                ), auto_commit=False)
            else:
                insert_cliente = """
                    INSERT INTO cliente (nombre, numero_documento, tipoDocumento, telefono, email, direccion)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                conexion.ejecutar(insert_cliente, (
                    contacto.get("razon_social"),
                    contacto.get("ruc"),
                    TipoDocumento.obtener_por_nombre(contacto.get("tipo_documento")),
                    contacto.get("telefono"),
                    contacto.get("email"),
                    contacto.get("direccion")
                ), auto_commit=False)

            id_cliente = conexion.cursor.lastrowid
            montoVenta = 100

            # 2. Registrar VENTA
            if pago.get("datos_especificos")["codigo_promocional"]:
                codPromo = Promocion.obtener_por_codigo(pago.get("datos_especificos")["codigo_promocional"])
                insert_venta = """
                    INSERT INTO venta (idCliente, fecha, subTotal, igv, idMetodoPago, idTipoComprobante, idPromocion)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                conexion.ejecutar(insert_venta, (
                    id_cliente,
                    datetime.now(),
                    0.0,
                    0.0,
                    pago.get("metodo_especifico"),
                    contacto.get("tipo_comprobante"),
                    codPromo
                ), auto_commit=False)
            else:
                insert_venta = """
                    INSERT INTO venta (idCliente, fecha, subTotal, igv, idMetodoPago, idTipoComprobante)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                conexion.ejecutar(insert_venta, (
                    id_cliente,
                    datetime.now(),
                    0.0,
                    0.0,
                    pago.get("metodo_especifico"),
                    contacto.get("tipo_comprobante")
                ), auto_commit=False)

            id_venta = conexion.cursor.lastrowid

            # 3. Registrar PASAJEROS, PASAJE y DETALLE_PASAJE
            for key, pasajero in ventas.items():
                insert_pasajero = """
                    INSERT INTO pasajero (nombre, ape_paterno, ape_materno, numero_documento, idTipoDocumento, sexo, f_nacimiento, telefono, email)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                conexion.ejecutar(insert_pasajero, (
                    pasajero.get("nombres"),
                    pasajero.get("apellidoPaterno"),
                    pasajero.get("apellidoMaterno"),
                    pasajero.get("numDoc"),
                    TipoDocumento.obtener_por_nombre(pasajero.get("tipoDoc")),
                    pasajero.get("sexo"),
                    pasajero.get("fechaNacimiento"),
                    pasajero.get("telefono"),
                    pasajero.get("correo")
                ), auto_commit=False)

                id_pasajero = conexion.cursor.lastrowid

                insert_pasaje = """
                    INSERT INTO pasaje (
                        idDetalleViajeAsiento,
                        numeroComprobante,
                        esPasajeNormal,
                        esPasajeLibre,
                        esTransferencia,
                        esReserva,
                        esCambioRuta,
                        idVenta,
                        codigo,
                        enTransaccion,
                        codigoReserva,
                        fecha_reserva
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)
                """
                conexion.ejecutar(insert_pasaje, (
                    key,
                    Pasaje.generar_numComprobante(),
                    0,  # esPasajeNormal
                    0,  # esPasajeLibre
                    0,  # esTransferencia
                    1,  # esReserva
                    0,  # esCambioRuta
                    id_venta,
                    Pasaje.generar_codigo_unico(),
                    0,  # enTransaccion
                    codigoReserva,
                    fecha
                ), auto_commit=False)

                id_pasaje = conexion.cursor.lastrowid

                insert_detalle = """
                    INSERT INTO detalle_pasaje (idPasajero, idPasaje, esMenorEdad, viajeEnBrazos, fecha_registro)
                    VALUES (%s, %s, %s, %s, %s)
                """
                conexion.ejecutar(insert_detalle, (
                    id_pasajero,
                    id_pasaje,
                    int(pasajero.get("esMenor", False)),
                    int(pasajero.get("brazos", False)),
                    datetime.now()
                ), auto_commit=False)

            conexion.conn.commit()
            return {"status": 1, "msg": "Reserva registrada correctamente", "id_venta": id_venta}

        except Exception as e:
            conexion.conn.rollback()
            return {"status": -1, "msg": f"Error al registrar reserva: {str(e)}"}

        finally:
            conexion.cerrar()
