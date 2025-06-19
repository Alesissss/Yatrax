import bd

class Reembolso:
    def __init__(self, id=None, numeroComprobante=None, monto=None, fecha=None,
                 idPasaje=None, idCliente=None, idTipoComprobante=None, idMetodoPago=None):
        self.id = id
        self.numeroComprobante = numeroComprobante
        self.monto = monto
        self.fecha = fecha
        self.idPasaje = idPasaje
        self.idCliente = idCliente
        self.idTipoComprobante = idTipoComprobante
        self.idMetodoPago = idMetodoPago

    # Obtener todos los reembolsos
    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            reembolsos = conexion.obtener("""
                SELECT r.id, r.numeroComprobante, r.monto, r.fecha,
                       r.idPasaje, r.idCliente, r.idTipoComprobante, r.idMetodoPago
                FROM reembolso r
            """)
            return reembolsos
        finally:
            conexion.cerrar()

    # Obtener un reembolso por ID
    @classmethod
    def obtener_por_id(cls, reembolso_id):
        conexion = bd.Conexion()
        try:
            reembolso = conexion.obtener("""
                SELECT r.id, r.numeroComprobante, r.monto, r.fecha,
                       r.idPasaje, r.idCliente, r.idTipoComprobante, r.idMetodoPago
                FROM reembolso r
                WHERE r.id = %s
            """, (reembolso_id,))
            return reembolso[0] if reembolso else None
        finally:
            conexion.cerrar()

    # Registrar un nuevo reembolso
    @classmethod
    def registrar(cls, numeroComprobante, monto, idPasaje, idCliente, idTipoComprobante, idMetodoPago):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar(
                "CALL SP_REGISTRAR_REEMBOLSO(%s, %s, %s, %s, %s, %s);",
                (numeroComprobante, monto, idPasaje, idCliente, idTipoComprobante, idMetodoPago)
            )
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # {'@MSJ': '...', '@MSJ2': '...'}
        finally:
            conexion.cerrar()
