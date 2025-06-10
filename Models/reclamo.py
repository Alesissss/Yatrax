import hashlib
import bd

class Reclamo:
    def __init__(self, id, tipo_reclamo, detalle, monto, id_pasaje, motivo):
        self.id = id
        self.tipo_reclamo = tipo_reclamo
        self.detalle = detalle
        self.monto = monto
        self.id_pasaje = id_pasaje
        self.motivo = motivo

    @classmethod
    def obtener_todos(cls):
        conexion = None
        try:
            conexion = bd.Conexion()
            return conexion.obtener("SELECT * FROM reclamo")
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, id):
        conexion = None
        try:
            conexion = bd.Conexion()
            resultados = conexion.obtener(
                "SELECT * FROM reclamo WHERE id = %s",
                (id,)
            )
            return resultados[0] if resultados else None
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def registrar(cls, tipo_reclamo, detalle, monto, id_pasaje, motivo):
        conexion = None
        try:
            conexion = bd.Conexion()
            # Llamada al SP con variables de usuario para los OUT
            conexion.ejecutar(
                "CALL SP_INSERTAR_RECLAMO(%s, %s, %s, %s, %s, @MSJ, @MSJ2)",
                (tipo_reclamo, detalle, monto, id_pasaje, motivo)
            )
            resultado = conexion.obtener("SELECT @MSJ AS MSJ, @MSJ2 AS MSJ2")
            return resultado[0] if resultado else None
        except Exception as e:
            return {"Status": 0, "Mensaje": f"Error: {e}"}
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def editar(cls, id, tipo_reclamo, detalle, monto, id_pasaje, motivo):
        conexion = None
        try:
            conexion = bd.Conexion()
            conexion.ejecutar(
                "CALL SP_MODIFICAR_RECLAMO(%s, %s, %s, %s, %s, %s, @MSJ, @MSJ2)",
                (id, tipo_reclamo, detalle, monto, id_pasaje, motivo)
            )
            resultado = conexion.obtener("SELECT @MSJ AS MSJ, @MSJ2 AS MSJ2")
            return resultado[0] if resultado else None
        except Exception as e:
            return {"Status": 0, "Mensaje": f"Error: {e}"}
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def eliminar(cls, id):
        conexion = None
        try:
            conexion = bd.Conexion()
            conexion.ejecutar(
                "CALL SP_ELIMINAR_RECLAMO(%s, @MSJ, @MSJ2)",
                (id,)
            )
            resultado = conexion.obtener("SELECT @MSJ AS MSJ, @MSJ2 AS MSJ2")
            return resultado[0] if resultado else None
        except Exception as e:
            return {"Status": 0, "Mensaje": f"Error: {e}"}
        finally:
            if conexion:
                conexion.cerrar()
