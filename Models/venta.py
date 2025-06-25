from datetime import datetime
from Models.tipoDocumento import TipoDocumento
from Models.promocion import Promocion
from Models.pasaje import Pasaje
import bd  # Utilizamos tu clase Conexion personalizada

class Venta:
    @classmethod
    def registrar_operacion(cls, contacto: dict, pago: dict, ventas: dict):
        print(contacto)

        print(contacto)
        print(pago)
        print(ventas)
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
            montoVenta = 100
            if pago.get("datos_especificos")["codigo_promocional"]:
                codPromo = Promocion.obtener_por_codigo(pago.get("datos_especificos")["codigo_promocional"])
                insert_venta = """
                    INSERT INTO venta (idCliente, fecha, subTotal, igv, idMetodoPago, idTipoComprobante, idPromocion)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                conexion.ejecutar(insert_venta, (
                    id_cliente,
                    datetime.now(),
                    0.0,  # Puedes calcularlo luego
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
                    0.0,  # Puedes calcularlo luego
                    0.0,
                    pago.get("metodo_especifico"),
                    contacto.get("tipo_comprobante")
                ), auto_commit=False)
            # 2. Registrar VENTA
            print(2)
            id_venta = conexion.cursor.lastrowid

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
                conexion.ejecutar(insert_pasaje, (
                    # idDetalleViajeAsiento
                    key,
                    # numroComprobante
                    Pasaje.generar_numComprobante(),
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
            return {"status": 1, "msg": "Venta registrada correctamente", "id_venta": id_venta}

        except Exception as e:
            conexion.conn.rollback()
            return {"status": -1, "msg": f"Error al registrar venta: {str(e)}"}

        finally:
            conexion.cerrar()


    @classmethod
    def registrar_operacion_ruta(cls, contacto: dict, pago: dict, ventas: dict):
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
            montoVenta = 100
            if pago.get("datos_especificos")["codigo_promocional"]:
                codPromo = Promocion.obtener_por_codigo(pago.get("datos_especificos")["codigo_promocional"])
                insert_venta = """
                    INSERT INTO venta (idCliente, fecha, subTotal, igv, idMetodoPago, idTipoComprobante, idPromocion)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                conexion.ejecutar(insert_venta, (
                    id_cliente,
                    datetime.now(),
                    0.0,  # Puedes calcularlo luego
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
                    0.0,  # Puedes calcularlo luego
                    0.0,
                    pago.get("metodo_especifico"),
                    contacto.get("tipo_comprobante")
                ), auto_commit=False)
            # 2. Registrar VENTA
            print(2)
            id_venta = conexion.cursor.lastrowid
            # ADICIONAL PARA UPDATE
            
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
                conexion.ejecutar(insert_pasaje, (
                    # idDetalleViajeAsiento
                    key,
                    # numroComprobante
                    Pasaje.generar_numComprobante(),
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
            return {"status": 1, "msg": "Venta registrada correctamente", "id_venta": id_venta}

        except Exception as e:
            conexion.conn.rollback()
            return {"status": -1, "msg": f"Error al registrar venta: {str(e)}"}

        finally:
            conexion.cerrar()

    @classmethod
    def obtener_reporte_ventas(cls):
        try:
            conexion = bd.Conexion()
            result = conexion.obtener(""" SELECT c.nombre, c.ape_paterno, c.ape_materno, v.fecha, sum(subtotal + igv) as totalMonto, count(p.id) as totalPasajes
                FROM venta v 
                INNER JOIN cliente c on v.idCliente = c.id 
                INNER JOIN pasaje p on p.idVenta = v.id
                -- WHERE p.esPasajeNormal = 1
                GROUP BY c.nombre, c.ape_paterno, c.ape_materno, v.fecha """)
            
            return result
        finally:
            conexion.cerrar()