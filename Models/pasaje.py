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
    def listarReservas(cls):
        conexion = None
        try:
            conexion = bd.Conexion()
            listado = conexion.obtener("select * from pasaje where estado='R'")
            return listado
        finally:
            if conexion != None:
                conexion.cerrar()

    @classmethod
    def obtener_una_reserva(cls,id):
        conexion = None
        try:
            conexion = bd.Conexion()
            reserva = conexion.obtener("select * from pasaje where estado='R' and id=%s",(id,))
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



