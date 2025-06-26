from datetime import datetime
from Models.tipoDocumento import TipoDocumento
from Models.promocion import Promocion
from Models.pasaje import Pasaje
from pdfGenerator import TicketTransporteSimple
from generadorQR import generar_codigo_qr
import bd  # Utilizamos tu clase Conexion personalizada

class Venta:

    @classmethod
    def registrar_operacion(cls, contacto: dict, pago: dict, ventas: dict):
        conexion = bd.Conexion()
        try:
            # TIPO COMPROBANTE 1 == BOLETA ,  2 == FACTURA
            if(contacto.get("tipo_comprobante") == "1"):
            # 1. Registrar CLIENTE
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
                    INSERT INTO cliente (nombre, numero_documento, tipoDocumento, telefono, email,direccion)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                conexion.ejecutar(insert_cliente, (
                contacto.get("razon_social"),
                contacto.get("ruc"),
                TipoDocumento.obtener_por_nombre(contacto.get("tipo_documento")),
                contacto.get("telefono"),
                contacto.get("email"),
                contacto.get("direccion")
                ), auto_commit=False)
            print(1)
            id_cliente = conexion.cursor.lastrowid
            sum = 0
            for key, pasajero in ventas.items():
                precio = pasajero.get("precio")
                # Convierte a float si es un número en formato de cadena
                sum += float(precio) if precio else 0
            montoVenta = sum
            if pago.get("datos_especificos")["codigo_promocional"]:
                codPromo = Promocion.obtener_por_codigo(pago.get("datos_especificos")["codigo_promocional"])
                insert_venta = """
                    INSERT INTO venta (idCliente, fecha, subTotal, igv, idMetodoPago, idTipoComprobante, idPromocion)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                conexion.ejecutar(insert_venta, (
                    id_cliente,
                    datetime.now(),
                    montoVenta,  # Puedes calcularlo luego
                    montoVenta*0.18,
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
                    0.0,  # Puedes calcularlo luego
                    0.0,
                    pago.get("metodo_especifico"),
                    contacto.get("tipo_comprobante")
                ), auto_commit=False)
            # 2. Registrar VENTA
            print(2)
            id_venta = conexion.cursor.lastrowid
            tickets_data = []
            # 3. Registrar PASAJEROS, PASAJE y DETALLE_PASAJE
            for key, pasajero in ventas.items():

                insert_pasajero = """
                    INSERT INTO pasajero (nombre, ape_paterno, ape_materno, numero_documento, idTipoDocumento, sexo, f_nacimiento, telefono, email)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                conexion.ejecutar(insert_pasajero, (
                    # nombre
                    pasajero.get("nombres"),
                    # ape_paterno
                    pasajero.get("apellidoPaterno"),
                    # ape_materno
                    pasajero.get("apellidoMaterno"),
                    # numero_doc
                    pasajero.get("numDoc"),
                    # id_tipo_doc
                    TipoDocumento.obtener_por_nombre(pasajero.get("tipoDoc")),
                    #sexo
                    pasajero.get("sexo"),
                    # fecha_nac
                    pasajero.get("fechaNacimiento"),
                    # telefono
                    pasajero.get("telefono"),
                    # email
                    pasajero.get("correo")
                ), auto_commit=False)
                id_pasajero = conexion.cursor.lastrowid
                print(3)
                insert_pasaje = """
                    INSERT INTO pasaje (idDetalleViajeAsiento, numeroComprobante, esPasajeNormal, esPasajeLibre, esTransferencia, esReserva, esCambioRuta, idVenta, codigo, enTransaccion)
                    VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s)
                """
                print(4)
                numComprobante = Pasaje.generar_numComprobante()
                codigoUnico = Pasaje.generar_codigo_unico()
                conexion.ejecutar(insert_pasaje, (
                    # idDetalleViajeAsiento
                    key,
                    # numroComprobante
                    numComprobante,
                    # esPasajeNormal
                    1,
                    # esPasajeLibre
                    0,
                    # esTransferencia
                    0,
                    # esReserva
                    0,
                    # esCambioRuta
                    0,
                    # idVenta
                    id_venta,
                    # codigo
                    codigoUnico,
                    # enTransaccion
                    0
                ), auto_commit=False)
                tickets_data.append({
                    "codigo":codigoUnico,
                    "numero_comprobante": numComprobante,
                    "asiento": key,
                    "pasajero": f"{pasajero.get('nombres')} {pasajero.get('apellidoPaterno')} {pasajero.get('apellidoMaterno')}",
                    "documento_pasajero": pasajero.get("numDoc"),
                    "precio_unitario": pasajero.get("precio"),  # si deseas calcularlo dinámico, cámbialo aquí
                    "fecha_viaje": "05/07/2025",  # pon aquí la real si la tienes
                    "hora_viaje": "04:06 PM"
                })
                id_pasaje = conexion.cursor.lastrowid
                print(4)
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
            print(5)
            conexion.conn.commit()
            ticket = TicketTransporteSimple()

            empresa = Venta.consultar_empresa_activa()
            rutas_pdf = []  # Lista para almacenar las rutas de los tickets generados
            for datos in tickets_data:
                num_boleta = datos["numero_comprobante"]
                cod_boleta = datos["codigo"]
                url_verificacion = f"http://see.transporteschiclayo.pe/verificar/{cod_boleta}"
                qr_path = generar_codigo_qr(url_verificacion, cod_boleta)

                datos_ticket = {
                    "empresa": {
                        "nombre": empresa["razon_social"],
                        "ruc": empresa["ruc"],
                        "direccion": empresa["direccion"],
                        "telefono": empresa["telefono"],
                        "tipo_comprobante": "BOLETA DE VENTA ELECTRÓNICA",
                        "numero_comprobante": num_boleta
                    },
                    "comprobante": {
                        "fecha": datetime.now().strftime("%d/%m/%Y"),
                        "hora": datetime.now().strftime("%H:%M:%S"),
                        "moneda": "PEN",
                        "cajero": "Web"
                    },
                    "cliente": {
                        "documento": contacto.get("numero_documento"),
                        "nombre": f"{contacto.get('nombres')} {contacto.get('apellido_paterno')} {contacto.get('apellido_materno')}"
                    },
                    "viaje": {
                        "embarque": "Por determinar",
                        "desembarque": "Por determinar",
                        "codigo": cod_boleta
                    },
                    "servicio": {
                        "ruta": "CHICLAYO-LIMA",
                        "tipo_servicio": "BUS CAMA",
                        "asiento": datos["asiento"],
                        "pasajero": datos["pasajero"],
                        "documento_pasajero": datos["documento_pasajero"],
                        "fecha_viaje": datos["fecha_viaje"],
                        "hora_viaje": datos["hora_viaje"],
                        "cantidad": 1,
                        "precio_unitario": float(datos["precio_unitario"]),
                        "total": float(datos["precio_unitario"])
                    },
                    "totales": {
                        "op_gravada": 0.00,
                        "op_exonerada": float(datos["precio_unitario"]),
                        "igv": float(montoVenta*0.18),
                        "descuento": 0.00,
                        "total": float(montoVenta)
                    },
                    "total_letras": "CIEN Y 00/100 SOLES",  # O usa una función que convierta a letras
                    "condicion_pago": "CONTADO",
                    "url": url_verificacion,
                    "qr": qr_path
                }

                ruta_ticket = ticket.generar_ticket(datos_ticket)  # Método que genera el PDF
                rutas_pdf.append(ruta_ticket)  # Agrega la ruta del archivo PDF a la lista
                print(rutas_pdf)
            # Devuelve las rutas generadas
            return {
                "status": 1,
                "msg": "Venta registrada correctamente",
                "id_venta": id_venta,
                "tickets": rutas_pdf  # Devuelves las rutas de todos los tickets generados
            }


        except Exception as e:
            conexion.conn.rollback()
            return {"status": -1, "msg": f"Error al registrar venta: {str(e)}"}

        finally:
            conexion.cerrar()

    @classmethod
    def registrar_operacion_x(cls, contacto: dict, pago: dict, ventas: dict):
        conexion = bd.Conexion()
        try:
            # TIPO COMPROBANTE 1 == BOLETA ,  2 == FACTURA
            if(contacto.get("tipo_comprobante") == "1"):
            # 1. Registrar CLIENTE
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
                    INSERT INTO cliente (nombre, numero_documento, tipoDocumento, telefono, email,direccion)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                conexion.ejecutar(insert_cliente, (
                contacto.get("razon_social"),
                contacto.get("ruc"),
                TipoDocumento.obtener_por_nombre(contacto.get("tipo_documento")),
                contacto.get("telefono"),
                contacto.get("email"),
                contacto.get("direccion")
                ), auto_commit=False)
            print(1)
            id_cliente = conexion.cursor.lastrowid
            if pago.get("datos_especificos")["codigo_promocional"]:
                codPromo = Promocion.obtener_por_codigo(pago.get("datos_especificos")["codigo_promocional"])
                insert_venta = """
                    INSERT INTO venta (idCliente, fecha, subTotal, igv, idMetodoPago, idTipoComprobante, idPromocion)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                conexion.ejecutar(insert_venta, (
                    id_cliente,
                    datetime.now(),
                    0, # Puedes calcularlo luego
                    0,
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
                    0.0,  # Puedes calcularlo luego
                    0.0,
                    pago.get("metodo_especifico"),
                    contacto.get("tipo_comprobante")
                ), auto_commit=False)
            # 2. Registrar VENTA
            print(2)
            id_venta = conexion.cursor.lastrowid
            tickets_data = []
            # 3. Registrar PASAJEROS, PASAJE y DETALLE_PASAJE
            for key, pasajero in ventas.items():

                insert_pasajero = """
                    INSERT INTO pasajero (nombre, ape_paterno, ape_materno, numero_documento, idTipoDocumento, sexo, f_nacimiento, telefono, email)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                conexion.ejecutar(insert_pasajero, (
                    # nombre
                    pasajero.get("nombres"),
                    # ape_paterno
                    pasajero.get("apellidoPaterno"),
                    # ape_materno
                    pasajero.get("apellidoMaterno"),
                    # numero_doc
                    pasajero.get("numDoc"),
                    # id_tipo_doc
                    TipoDocumento.obtener_por_nombre(pasajero.get("tipoDoc")),
                    #sexo
                    pasajero.get("sexo"),
                    # fecha_nac
                    pasajero.get("fechaNacimiento"),
                    # telefono
                    pasajero.get("telefono"),
                    # email
                    pasajero.get("correo")
                ), auto_commit=False)
                id_pasajero = conexion.cursor.lastrowid
                print(3)
                insert_pasaje = """
                    INSERT INTO pasaje (idDetalleViajeAsiento, numeroComprobante, esPasajeNormal, esPasajeLibre, esTransferencia, esReserva, esCambioRuta, idVenta, codigo, enTransaccion)
                    VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s)
                """
                print(4)
                numComprobante = Pasaje.generar_numComprobante()
                conexion.ejecutar(insert_pasaje, (
                    # idDetalleViajeAsiento
                    key,
                    # numroComprobante
                    numComprobante,
                    # esPasajeNormal
                    1,
                    # esPasajeLibre
                    0,
                    # esTransferencia
                    0,
                    # esReserva
                    0,
                    # esCambioRuta
                    0,
                    # idVenta
                    id_venta,
                    # codigo
                    Pasaje.generar_codigo_unico(),
                    # enTransaccion
                    0
                ), auto_commit=False)
                tickets_data.append({
                    "numero_comprobante": numComprobante,
                    "asiento": key,
                    "pasajero": f"{pasajero.get('nombres')} {pasajero.get('apellidoPaterno')} {pasajero.get('apellidoMaterno')}",
                    "documento_pasajero": pasajero.get("numDoc"),
                    "precio_unitario": 0,  # si deseas calcularlo dinámico, cámbialo aquí
                    "fecha_viaje": "05/07/2025",  # pon aquí la real si la tienes
                    "hora_viaje": "04:06 PM"
                })
                id_pasaje = conexion.cursor.lastrowid
                print(4)
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
            print(5)
            conexion.conn.commit()
            
            # Devuelve las rutas generadas
            return {
                "status": 1,
                "msg": "Venta registrada correctamente",
                "id_venta": id_venta  # Devuelves las rutas de todos los tickets generados
            }


        except Exception as e:
            conexion.conn.rollback()
            print(str(e))
            return {"status": -1, "msg": f"Error al registrar venta: {str(e)}"}

        finally:
            conexion.cerrar()

    @classmethod
    def obtener_dashboard_ventas(cls):
        try:
            conexion = bd.Conexion()
            result = conexion.obtener(""" SELECT c.id, c.numero_documento, c.sexo, c.email, c.nombre, 
                c.ape_paterno, c.ape_materno, v.fecha, (subtotal + igv) as totalMonto, count(p.id) as totalPasajes
                FROM venta v 
                INNER JOIN cliente c on v.idCliente = c.id 
                INNER JOIN pasaje p on p.idVenta = v.id
                WHERE p.esPasajeNormal = 1
                GROUP BY c.id, c.numero_documento, c.sexo, c.email, c.nombre, c.ape_paterno, c.ape_materno, v.fecha, v.subtotal, v.igv """)
            
            return result
        finally:
            conexion.cerrar()

            
    @classmethod
    def obtener_reporte_puntualidad(cls, idRuta):
        try:
            conexion = bd.Conexion()
            result = conexion.obtener(
            """
                SELECT 
                    ru.nombre AS ruta,
                    CONCAT(UPPER(suo.nombre), ' - ', UPPER(suo.ciudad)) AS sucursalOrigen,
                    CONCAT(UPPER(sud.nombre), ' - ', UPPER(sud.ciudad)) AS sucursalDestino,
                    idViaje, 
                    idSucursalOrigen, 
                    idSucursalDestino, 
                    fechaSalida, 
                    fechaSalidaReal, 
                    TIMESTAMPDIFF(MINUTE, fechaSalida, fechaSalidaReal) AS minDiferenciaSalida, 
                    fechaLlegadaEstimada, 
                    fechaLlegadaReal, 
                    TIMESTAMPDIFF(MINUTE, fechaLlegadaEstimada, fechaLlegadaReal) AS minDiferenciaLlegada, 
                    CASE 
                        WHEN fechaSalida = fechaSalidaReal THEN 'Puntual' 
                        ELSE 'Retraso' 
                    END AS PuntualidadSalida, 
                    CASE 
                        WHEN fechaLlegadaEstimada = fechaLlegadaReal THEN 'Puntual' 
                        ELSE 'Retraso' 
                    END AS PuntualidadLlegada
                FROM 
                    detalle_viaje dv
                INNER JOIN 
                    viaje vi ON vi.id = dv.idViaje
                INNER JOIN 
                    ruta ru ON ru.id = vi.idRuta
                INNER JOIN 
                    sucursal suo ON suo.id = dv.idSucursalOrigen
                INNER JOIN 
                    sucursal sud ON sud.id = dv.idSucursalDestino
                WHERE ru.id = %s;
            """, (idRuta,))
            return result
        finally:
            conexion.cerrar()
    @classmethod
    def consultar_empresa_activa(cls):
        conexion = bd.Conexion()
        try:
            lista = conexion.obtener("SELECT * FROM empresa WHERE estado = 1")
            if lista: return lista[0]
        finally:
            conexion.cerrar()