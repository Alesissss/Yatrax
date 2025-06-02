import hashlib
import bd

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
    def registrarReserva(cls, id_metodo_pago, id_tipo_comprobante, id_cliente, id_promocion,id_viaje):
        conexion = None
        try:
            conexion = bd.Conexion()

            conexion.ejecutar("CALL SP_INSERTAR_PASAJE(%s, %s, %s, %s, %s,%s, @MSJ, @MSJ2);", (id_metodo_pago,id_tipo_comprobante,id_cliente,id_promocion,id_viaje,'R'))

            resultado = conexion.obtener("SELECT @MSJ AS msj, @MSJ2 AS msj2;")
            return resultado[0] if resultado else {"msj": None, "msj2": "Error al recuperar mensaje"}
        
        except Exception as e:
            return {"msj": None, "msj2": f"Error en la reserva: {str(e)}"}
        finally:
            if conexion != None:
                conexion.cerrar()

