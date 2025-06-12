import hashlib
import bd
import string
import random

class Pasaje:
    def __init__(self,id,id_metodo_pago,id_tipo_comprobante,id_cliente,id_promocion,id_viaje,estado):
        self.id = id
        self.id_metodo_pago = id_metodo_pago
        self.id_tipo_comprobante = id_tipo_comprobante
        self.id_cliente = id_cliente
        self.id_promocion = id_promocion
        self.id_viaje = id_viaje
        self.estado = estado

    @classmethod
    def listarReservas(cls):
        conexion = None
        try:
            conexion = bd.Conexion()
            listado = conexion.obtener("""
                SELECT 
                pas.id as id,
                pas.idVenta as id_venta,
                cli.nombre as cliente,
                cli.numero_documento as num_doc,
                suc_origen.nombre AS origen,
                suc_destino.nombre AS destino,
                pas.codigo as codigo,
                pas.esReserva as reserva,
                pas.esPasajeNormal as pagado
                FROM pasaje pas
                LEFT JOIN cliente cli ON pas.idCliente = cli.id
                LEFT JOIN detalle_viaje_asiento deta ON pas.idDetalleViajeAsiento = deta.id
                LEFT JOIN detalle_viaje det ON det.id = deta.idDetalle_Viaje
                LEFT JOIN sucursal suc_origen ON det.idSucursalOrigen = suc_origen.id
                LEFT JOIN sucursal suc_destino ON det.idSucursalDestino = suc_destino.id;
            """)
            return listado
        finally:
            if conexion != None:
                conexion.cerrar()

    @classmethod
    def obtener_una_reserva(cls,id):
        conexion = None
        try:
            conexion = bd.Conexion()
            reserva = conexion.obtener("select * from pasaje where esReserva=1 and id=%s",(id,))
            return reserva[0]
        finally:
            if conexion != None:
                conexion.cerrar()

    @classmethod
    def registrarReserva(cls, id_metodo_pago, id_tipo_comprobante, id_cliente, id_promocion,id_viaje,codigo):
        conexion = None
        try:
            conexion = bd.Conexion()

            conexion.ejecutar("CALL SP_INSERTAR_PASAJE(%s, %s, %s, %s, %s,%s,%s, @MSJ, @MSJ2);", (id_metodo_pago,id_tipo_comprobante,id_cliente,id_promocion,id_viaje,'R',codigo))

            resultado = conexion.obtener("SELECT @MSJ AS msj, @MSJ2 AS msj2;")
            return resultado[0] if resultado else {"msj": None, "msj2": "Error al recuperar mensaje"}
        
        except Exception as e:
            return {"msj": None, "msj2": f"Error en la reserva: {str(e)}"}
        finally:
            if conexion != None:
                conexion.cerrar()
    
    @classmethod
    def modificarReserva(cls, p_id, id_metodo_pago, id_tipo_comprobante, id_cliente, id_promocion, id_viaje, estado):
        conexion = None
        try:
            conexion = bd.Conexion()

            # Llamamos al procedimiento SP_MODIFICAR_PASAJE con sus parámetros y recuperamos los parámetros de salida @MSJ y @MSJ2
            conexion.ejecutar(
                "CALL SP_MODIFICAR_PASAJE(%s, %s, %s, %s, %s, %s,%s, @MSJ, @MSJ2);",
                (p_id, id_metodo_pago, id_tipo_comprobante, id_cliente, id_promocion, id_viaje, estado)
            )

            resultado = conexion.obtener("SELECT @MSJ AS msj, @MSJ2 AS msj2;")
            return resultado[0] if resultado else {"msj": None, "msj2": "Error al recuperar mensaje"}
        
        except Exception as e:
            return {"msj": None, "msj2": f"Error al modificar pasaje: {str(e)}"}
        
        finally:
            if conexion is not None:
                conexion.cerrar()

    @classmethod
    def eliminarReserva(cls, p_id):
        conexion = None
        try:
            conexion = bd.Conexion()

            conexion.ejecutar(
                "CALL SP_ELIMINAR_PASAJE(%s, @MSJ, @MSJ2);",
                (p_id,)
            )

            resultado = conexion.obtener("SELECT @MSJ AS msj, @MSJ2 AS msj2;")
            return resultado[0] if resultado else {"msj": None, "msj2": "Error al recuperar mensaje"}
        
        except Exception as e:
            return {"msj": None, "msj2": f"Error al eliminar pasaje: {str(e)}"}
        
        finally:
            if conexion is not None:
                conexion.cerrar()

    @classmethod
    def cambiarEstado(cls, id_pasaje, nuevo_estado):
        conexion = None
        try:
            conexion = bd.Conexion()
            # Llamamos con 2 parámetros de entrada + 2 parámetros OUT implicados
            conexion.ejecutar(
                "CALL SP_CAMBIAR_ESTADO_PASAJE(%s, %s, @MSJ, @MSJ2);",
                (id_pasaje, nuevo_estado)
            )
            resultado = conexion.obtener("SELECT @MSJ AS msj, @MSJ2 AS msj2;")
            return resultado[0] if resultado else {"msj": None, "msj2": "Error al recuperar mensaje"}
        except Exception as e:
            return {"msj": None, "msj2": f"Error en el modelo: {str(e)}"}
        finally:
            if conexion is not None:
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
    
    



