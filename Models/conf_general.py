import bd

class ConfGeneral:
    def __init__(self, id=None, igv=None, tarifaBase=None, max_pasajes_venta=None, tiempo_maximo_venta_minutos=None, viajesReprogramables=None, maxDiasReprogramacion=None, precioCambioRuta=None, precioTransferencia=None):
        self.id = id
        self.igv = igv
        self.tarifaBase = tarifaBase
        self.max_pasajes_venta = max_pasajes_venta
        self.tiempo_maximo_venta_minutos = tiempo_maximo_venta_minutos
        self.viajesReprogramables = viajesReprogramables
        self.maxDiasReprogramacion = maxDiasReprogramacion
        self.precioCambioRuta = precioCambioRuta
        self.precioTransferencia = precioTransferencia

    @classmethod
    def obtener(cls):
        conexion = bd.Conexion()
        try:
            conf_general = conexion.obtener("SELECT * FROM conf_general LIMIT 1")
            return conf_general[0] if conf_general else None
        finally:
            conexion.cerrar()

    @classmethod
    def modificar(cls, igv, tarifaBase, max_pasajes_venta, tiempo_maximo_venta_minutos, viajesReprogramables, max_dias_reprogramacion, precioCambioRuta, precioTransferencia):
        conexion = bd.Conexion()

        try:
            conexion.ejecutar("CALL SP_MODIFICAR_CONF_GENERAL(%s, %s, %s, %s, %s, %s, %s, %s);", 
                              (igv, tarifaBase, max_pasajes_venta, tiempo_maximo_venta_minutos, viajesReprogramables, max_dias_reprogramacion, precioCambioRuta, precioTransferencia))

            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()
