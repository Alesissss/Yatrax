from datetime import datetime
from Models.tipoDocumento import TipoDocumento
from Models.tipoComprobante import TipoComprobante
from Models.promocion import Promocion
from Models.pasaje import Pasaje
from Models.cliente import Cliente
from pdfGenerator import TicketTransporteSimple
from generadorQR import generar_codigo_qr
from num2words import num2words
from Models.asiento import Asiento
import bd  # Utilizamos tu clase Conexion personalizada

class Venta:

    @classmethod
    def registrar_operacion(cls, contacto: dict, pago: dict, ventas: dict):
        conexion = bd.Conexion()
        rutas_pdf_generadas = [] # Lista para almacenar las rutas de los tickets generados
        try:
            IGV = pago.get("igv")
            conexion.conn.begin()

            id_cliente = Cliente.obtener_id_por_numero_documento(contacto.get("numero_documento"))
            if id_cliente:
                id_cliente = id_cliente["id"]
                nombre_cliente = Cliente.obtener_por_id(id_cliente).get("nombre")
            else:
                if contacto.get("tipo_comprobante") == "1": # Boleta
                    nombre_cliente = f"{contacto.get('nombres')} {contacto.get('apellido_paterno')} {contacto.get('apellido_materno')}"
                    insert_cliente_sql = """
                        INSERT INTO cliente (nombre, ape_paterno, ape_materno, numero_documento, id_tipo_doc, telefono, email)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """
                    conexion.ejecutar(insert_cliente_sql, (
                        contacto.get("nombres"),
                        contacto.get("apellido_paterno"),
                        contacto.get("apellido_materno"),
                        contacto.get("numero_documento"),
                        TipoDocumento.obtener_por_nombre(contacto.get("tipo_documento")),
                        contacto.get("telefono"),
                        contacto.get("email")
                    ), auto_commit=False)
                else: # Factura
                    nombre_cliente = contacto.get("razon_social")
                    insert_cliente_sql = """
                        INSERT INTO cliente (nombre, numero_documento, tipoDocumento, telefono, email, direccion)
                        VALUES (%s, %s, %s, %s, %s, %s)
                    """
                    conexion.ejecutar(insert_cliente_sql, (
                        contacto.get("razon_social"),
                        contacto.get("ruc"),
                        TipoDocumento.obtener_por_nombre(contacto.get("tipo_documento")),
                        contacto.get("telefono"),
                        contacto.get("email"),
                        contacto.get("direccion")
                    ), auto_commit=False)
                id_cliente = conexion.cursor.lastrowid
            
            nombre_comprobante = TipoComprobante.obtener_por_id(contacto.get("tipo_comprobante"))["nombre"]

            cod_promocion = None
            if pago.get("datos_especificos") and pago.get("datos_especificos").get("codigo_promocional"):
                cod_promocion = Promocion.obtener_por_codigo(pago.get("datos_especificos")["codigo_promocional"])
                insert_venta_sql = """
                    INSERT INTO venta (idCliente, subTotal, igv, idMetodoPago, idTipoComprobante, idPromocion)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """
                conexion.ejecutar(insert_venta_sql, (
                    id_cliente, 0.0, 0.0,
                    pago.get("metodo_especifico"),
                    contacto.get("tipo_comprobante"),
                    cod_promocion
                ), auto_commit=False)
            else:
                insert_venta_sql = """
                    INSERT INTO venta (idCliente, subTotal, igv, idMetodoPago, idTipoComprobante)
                    VALUES (%s, %s, %s, %s, %s)
                """
                conexion.ejecutar(insert_venta_sql, (
                    id_cliente, 0.0, 0.0,
                    pago.get("metodo_especifico"),
                    contacto.get("tipo_comprobante")
                ), auto_commit=False)

            id_venta = conexion.cursor.lastrowid
            monto_venta_total = 0

            # Datos generales para el ticket
            generales = {
                "nom_comprobante": nombre_comprobante,
                "cliente_doc": contacto.get("numero_documento"),
                "cliente_nom": nombre_cliente
            }
            empresa = Venta.consultar_empresa_activa()

            for key_asiento, pasajero_data in ventas.items():
                precio = pasajero_data.get("precio")
                monto_venta_total += float(precio) if precio else 0.0

                insert_pasajero_sql = """
                    INSERT INTO pasajero (nombre, ape_paterno, ape_materno, numero_documento, idTipoDocumento, sexo, f_nacimiento, telefono, email)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                conexion.ejecutar(insert_pasajero_sql, (
                    pasajero_data.get("nombres"),
                    pasajero_data.get("apellidoPaterno"),
                    pasajero_data.get("apellidoMaterno"),
                    pasajero_data.get("numDoc"),
                    TipoDocumento.obtener_por_nombre(pasajero_data.get("tipoDoc")),
                    pasajero_data.get("sexo"),
                    pasajero_data.get("fechaNacimiento"),
                    pasajero_data.get("telefono"),
                    pasajero_data.get("correo")
                ), auto_commit=False)
                id_pasajero = conexion.cursor.lastrowid

                num_comprobante_pasaje = Pasaje.generar_numComprobante()
                codigo_unico_pasaje = Pasaje.generar_codigo_unico()
                
                datos_asiento = Asiento.obtener_datos_asiento(key_asiento)
                datos_ruta = Asiento.obtener_datos_viaje(key_asiento)
                
                precio_float = float(precio) if precio else 0.0
                igv_float = float(IGV) if IGV is not None else 0.0

                subtotal_asiento_calc = precio_float / (1 + igv_float) if (1 + igv_float) != 0 else precio_float
                igv_asiento_calc = precio_float - subtotal_asiento_calc
                total_asiento_calc = precio_float

                # Preparar datos para generar el ticket individual
                datos_ticket_individual = { 
                    "codigo": codigo_unico_pasaje,
                    "numero_comprobante": num_comprobante_pasaje,
                    "asiento_id": key_asiento,
                    "asiento_nombre": datos_asiento.get("nombre_asiento", "N/A"),
                    "pasajero": f"{pasajero_data.get('nombres', '')} {pasajero_data.get('apellidoPaterno', '')} {pasajero_data.get('apellidoMaterno', '')}",
                    "documento_pasajero": pasajero_data.get("numDoc", "N/A"),
                    "subtotal_asiento": subtotal_asiento_calc,
                    "igv_asiento": igv_asiento_calc,
                    "total_asiento": total_asiento_calc,
                    "embarque": datos_ruta.get("embarque", "N/A"),
                    "ruta": datos_ruta.get("ruta", "N/A"),
                    "tipo_servicio": datos_asiento.get("tipo_asiento", "N/A"),
                    "desembarque": datos_ruta.get("desembarque", "N/A"),
                    "fecha_viaje": datos_ruta.get("fecha_salida", "N/A"),
                    "hora_viaje": datos_ruta.get("hora_salida","N/A")
                }

                # Generar el ticket y obtener su ruta
                ruta_ticket_generado = Venta.crearTicketIndividual(datos_ticket_individual, empresa, generales)
                rutas_pdf_generadas.append(ruta_ticket_generado)

                insert_pasaje_sql = """
                    INSERT INTO pasaje (idDetalleViajeAsiento, numeroComprobante, esPasajeNormal, esPasajeLibre, esTransferencia, esReserva, esCambioRuta, idVenta, codigo, enTransaccion, precio, rutaTicket)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                conexion.ejecutar(insert_pasaje_sql, (
                    key_asiento, num_comprobante_pasaje, 1, 0, 0, 0, 0,
                    id_venta, codigo_unico_pasaje, 0, precio, ruta_ticket_generado # Se inserta la ruta del ticket aquí
                ), auto_commit=False)
                id_pasaje = conexion.cursor.lastrowid

                insert_detalle_sql = """
                    INSERT INTO detalle_pasaje (idPasajero, idPasaje, esMenorEdad, viajeEnBrazos)
                    VALUES (%s, %s, %s, %s)
                """
                conexion.ejecutar(insert_detalle_sql, (
                    id_pasajero,
                    id_pasaje,
                    int(pasajero_data.get("esMenor", False)),
                    int(pasajero_data.get("brazos", False))
                ), auto_commit=False)

            if IGV is not None:
                total_venta_bruto = monto_venta_total
                subtotal_venta = total_venta_bruto / (1 + float(IGV)) if (1 + float(IGV)) != 0 else total_venta_bruto
                igv_venta_total = total_venta_bruto - subtotal_venta
            else:
                subtotal_venta = monto_venta_total
                igv_venta_total = 0.0

            conexion.ejecutar("UPDATE VENTA SET subTotal = %s, igv = %s WHERE id = %s",
                               (subtotal_venta, igv_venta_total, id_venta), auto_commit=False)
            
            conexion.conn.commit()
            return {
                "status": 1,
                "msg": "Venta registrada correctamente",
                "id_venta": id_venta,
                "tickets": rutas_pdf_generadas # Retorna las rutas de todos los tickets generados
            }
        
        except Exception as e:
            conexion.conn.rollback()
            return {"status": -1, "msg": f"Error al registrar venta: {str(e)}"}
        finally:
            conexion.cerrar()

    @classmethod
    def registrar_operacion_x(cls, contacto:    dict, pago: dict, ventas: dict, precio_venta_total: float = 0.0, datos_viaje: dict = None):
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
            id_cliente = conexion.cursor.lastrowid
            
            # Calcular IGV del precio total recibido (solo si el precio es mayor a 0)
            if precio_venta_total > 0:
                subtotal = precio_venta_total / 1.18  # Descomponer el precio total
                igv = precio_venta_total - subtotal
            else:
                # Si no hay precio, calcular desde ventas como fallback
                sum_ventas = 0
                for key, pasajero in ventas.items():
                    precio = pasajero.get("precio", 0)
                    sum_ventas += float(precio) if precio else 0
                subtotal = sum_ventas / 1.18 if sum_ventas > 0 else 0
                igv = sum_ventas - subtotal if sum_ventas > 0 else 0
            
            if pago.get("datos_especificos") and pago.get("datos_especificos").get("codigo_promocional"):
                codPromo = Promocion.obtener_por_codigo(pago.get("datos_especificos")["codigo_promocional"])
                insert_venta = """
                    INSERT INTO venta (idCliente, fecha, subTotal, igv, idMetodoPago, idTipoComprobante, idPromocion)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                conexion.ejecutar(insert_venta, (
                    id_cliente,
                    datetime.now(),
                    subtotal,  # Usar el subtotal calculado
                    igv,       # Usar el IGV calculado
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
                    subtotal,  # Usar el subtotal calculado
                    igv,       # Usar el IGV calculado
                    pago.get("metodo_especifico"),
                    contacto.get("tipo_comprobante")
                ), auto_commit=False)
            # 2. Registrar VENTA
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
                insert_pasaje = """
                    INSERT INTO pasaje (idDetalleViajeAsiento, numeroComprobante, esPasajeNormal, esPasajeLibre, esTransferencia, esReserva, esCambioRuta, idVenta, codigo, enTransaccion, precio)
                    VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s)
                """
                numComprobante = Pasaje.generar_numComprobante()
                codigoUnico = Pasaje.generar_codigo_unico()
                
                # Calcular precio por pasajero
                precio_pasajero = pasajero.get("precio", 0)
                if not precio_pasajero and precio_venta_total > 0:
                    # Si no hay precio individual, dividir el total entre el número de pasajeros
                    precio_pasajero = precio_venta_total / len(ventas)
                
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
                    0,
                    # precio
                    float(precio_pasajero)
                ), auto_commit=False)
                tickets_data.append({
                    "codigo": codigoUnico,
                    "numero_comprobante": numComprobante,
                    "asiento": key,
                    "pasajero": f"{pasajero.get('nombres')} {pasajero.get('apellidoPaterno')} {pasajero.get('apellidoMaterno')}",
                    "documento_pasajero": pasajero.get("numDoc"),
                    "precio_unitario": float(precio_pasajero),  # Usar el precio calculado
                    "fecha_viaje": "05/07/2025",  # pon aquí la real si la tienes
                    "hora_viaje": "04:06 PM"
                })
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
            
            # Generar tickets PDF
            ticket = TicketTransporteSimple()
            empresa = Venta.consultar_empresa_activa()
            rutas_pdf = []  # Lista para almacenar las rutas de los tickets generados
            
            for datos in tickets_data:
                num_boleta = datos["numero_comprobante"]
                cod_boleta = datos["codigo"]  # Usar el código ya generado
                url_verificacion = f"http://see.transporteschiclayo.pe/verificar/{cod_boleta}"
                qr_path = generar_codigo_qr(url_verificacion, cod_boleta)

                # Determinar el nombre del cliente según el tipo de comprobante
                if contacto.get("tipo_comprobante") == "1":  # Boleta
                    nombre_cliente = f"{contacto.get('nombres')} {contacto.get('apellido_paterno')} {contacto.get('apellido_materno')}"
                    documento_cliente = contacto.get("numero_documento")
                else:  # Factura
                    nombre_cliente = contacto.get("razon_social")
                    documento_cliente = contacto.get("ruc")

                datos_ticket = {
                    "empresa": {
                        "nombre": empresa["razon_social"],
                        "ruc": empresa["ruc"],
                        "direccion": empresa["direccion"],
                        "telefono": empresa["telefono"],
                        "tipo_comprobante": "BOLETA DE VENTA ELECTRÓNICA" if contacto.get("tipo_comprobante") == "1" else "FACTURA ELECTRÓNICA",
                        "numero_comprobante": num_boleta
                    },
                    "comprobante": {
                        "fecha": datetime.now().strftime("%d/%m/%Y"),
                        "hora": datetime.now().strftime("%H:%M:%S"),
                        "moneda": "PEN",
                        "cajero": "Web"
                    },
                    "cliente": {
                        "documento": documento_cliente,
                        "nombre": nombre_cliente
                    },
                    "viaje": {
                        "embarque": datos_viaje.get("origen", "Por determinar") if datos_viaje else "Por determinar",
                        "desembarque": datos_viaje.get("destino", "Por determinar") if datos_viaje else "Por determinar",
                        "codigo": cod_boleta
                    },
                    "servicio": {
                        "ruta": f"{datos_viaje.get('ciudad_origen', 'CHICLAYO')}-{datos_viaje.get('ciudad_destino', 'LIMA')}" if datos_viaje else "CHICLAYO-LIMA",
                        "tipo_servicio": "BUS CAMA",
                        "origen": datos_viaje.get("origen", "Por determinar") if datos_viaje else "Por determinar",
                        "destino": datos_viaje.get("destino", "Por determinar") if datos_viaje else "Por determinar",
                        "asiento": datos["asiento"],
                        "pasajero": datos["pasajero"],
                        "documento_pasajero": datos["documento_pasajero"],
                        "fecha_viaje": datos_viaje.get("fechaSalida", datos["fecha_viaje"]) if datos_viaje else datos["fecha_viaje"],
                        "hora_viaje": datos_viaje.get("fechaSalida", datos["hora_viaje"]) if datos_viaje else datos["hora_viaje"],
                        "cantidad": 1,
                        "precio_unitario": float(datos["precio_unitario"]),
                        "total": float(datos["precio_unitario"])
                    },
                    "totales": {
                        "op_gravada": 0.00,
                        "op_exonerada": float(datos["precio_unitario"]),
                        "igv": 0.00,  # Siempre mostrar IGV 0 al cliente
                        "descuento": 0.00,
                        "total": float(datos["precio_unitario"])  # Total = subtotal + igv (pero se muestra como precio unitario)
                    },
                    "total_letras": "CIEN Y 00/100 SOLES",  # Se puede usar función que convierta a letras
                    "condicion_pago": "CONTADO",
                    "url": url_verificacion,
                    "qr": qr_path
                }

                ruta_ticket = ticket.generar_ticket(datos_ticket)  # Método que genera el PDF
                rutas_pdf.append(ruta_ticket)  # Agrega la ruta del archivo PDF a la lista
            
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
    def crearTicketIndividual(cls, datos_ticket_individual: dict, empresa: dict, generales: dict) -> str:
        ticket = TicketTransporteSimple()
        url_verificacion = f"http://localhost:5000/ecommerce/home/inicio"
        
        num_boleta = datos_ticket_individual["numero_comprobante"]
        cod_boleta = datos_ticket_individual["codigo"]
        
        qr_path = generar_codigo_qr(url_verificacion, cod_boleta)

        datos_para_pdf = {
            "empresa": {
                "nombre": empresa["razon_social"],
                "ruc": empresa["ruc"],
                "direccion": empresa["direccion"],
                "telefono": empresa["telefono"],
                "tipo_comprobante": f"{generales['nom_comprobante'].upper()} DE VENTA ELECTRÓNICA",
                "numero_comprobante": num_boleta
            },
            "comprobante": {
                "fecha": datetime.now().strftime("%d/%m/%Y"),
                "hora": datetime.now().strftime("%H:%M:%S"),
                "moneda": "PEN",
                "cajero": "Web"
            },
            "cliente": {
                "documento": generales["cliente_doc"].upper(),
                "nombre": generales["cliente_nom"].upper()
            },
            "viaje": {
                "embarque": datos_ticket_individual["embarque"].upper(),
                "desembarque": datos_ticket_individual["desembarque"].upper(),
                "codigo": cod_boleta
            },
            "servicio": {
                "ruta": datos_ticket_individual["ruta"].upper(),
                "tipo_servicio": datos_ticket_individual["tipo_servicio"].upper(),
                "asiento": datos_ticket_individual["asiento_nombre"].upper(),
                "pasajero": datos_ticket_individual["pasajero"].upper(),
                "documento_pasajero": datos_ticket_individual["documento_pasajero"].upper(),
                "fecha_viaje": datos_ticket_individual["fecha_viaje"],
                "hora_viaje": datos_ticket_individual["hora_viaje"],
                "cantidad": 1,
                "precio_unitario": float(datos_ticket_individual["subtotal_asiento"]),
                "total": float(datos_ticket_individual["total_asiento"])
            },
            "totales": {
                "op_gravada": 0.00,
                "op_exonerada": float(datos_ticket_individual["subtotal_asiento"]),
                "igv": float(datos_ticket_individual["igv_asiento"]),
                "descuento": 0.00,
                "total": float(datos_ticket_individual["total_asiento"])
            },
            "total_letras": Venta.numero_a_soles_texto(float(datos_ticket_individual["total_asiento"])).upper(),
            "condicion_pago": "CONTADO",
            "url": url_verificacion,
            "qr": qr_path
        }
        ruta_ticket = ticket.generar_ticket(datos_para_pdf) # Asumo que este método retorna la ruta del PDF
        return ruta_ticket

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
    
    @classmethod
    def numero_a_soles_texto(cls,numero: float):

        parte_entera = int(numero)
        # Redondear para evitar problemas de coma flotante, luego multiplicar por 100
        parte_decimal = int(round((numero - parte_entera) * 100))

        texto_soles = num2words(parte_entera, lang='es')
        texto_centimos = num2words(parte_decimal, lang='es')

        # Determinar si es "sol" o "soles"
        if parte_entera == 1:
            unidad_sol = "sol"
        else:
            unidad_sol = "soles"

        # Determinar si es "céntimo" o "céntimos"
        if parte_decimal == 1:
            unidad_centimo = "céntimo"
        else:
            unidad_centimo = "céntimos"

        # Construir el resultado final
        if parte_decimal == 0:
            return f"{texto_soles} {unidad_sol}"
        elif parte_entera == 0:
            return f"{texto_centimos} {unidad_centimo}"
        else:
            return f"{texto_soles} {unidad_sol} con {texto_centimos} {unidad_centimo}"