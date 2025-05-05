import hashlib
import bd
from datetime import timedelta

class horario:
    def __init__(self, id=None, horario_entrada=None, horario_salida=None, estado=None, estado_proceso=None, estado_registro=None, fecha_registro=None):
        self.id = id
        self.horario_entrada = horario_entrada
        self.horario_salida = horario_salida
        self.estado = estado
        #Auditoría
        self.estado_proceso = estado_proceso
        self.estado_registro = estado_registro
        self.fecha_registro = fecha_registro

    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            horarios = conexion.obtener("SELECT id, horario_entrada, horario_salida, estado FROM horario where estado_registro = 1")
            def formatear_tiempo(td):
                if isinstance(td, timedelta):
                    total_segundos = int(td.total_seconds())
                    horas = total_segundos // 3600
                    minutos = (total_segundos % 3600) // 60
                    segundos = total_segundos % 60
                    return f"{horas:02d}:{minutos:02d}:{segundos:02d}"
                return str(td)
            for h in horarios:
                h['horario_entrada'] = formatear_tiempo(h['horario_entrada'])
                h['horario_salida'] = formatear_tiempo(h['horario_salida'])
            return horarios
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, horario_id):
        conexion = bd.Conexion()
        try:
            horario = conexion.obtener(f"SELECT id, horario_entrada, horario_salida, estado, estado_proceso FROM horario WHERE id = {horario_id}")
            return horario[0] if horario else None
        finally:
            conexion.cerrar()

    #REGISTRAR
    @classmethod
    def registrar(cls,horario_entrada, horario_salida, estado):
        conexion = bd.Conexion()
        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_REGISTRAR_horario(%s, %s, %s);", (horario_entrada, horario_salida, estado))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()

    #EDITAR
    @classmethod
    def editar(cls, id, horario_entrada, horario_salida, estado):
        conexion = bd.Conexion()

        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_EDITAR_HORARIO(%s, %s, %s, %s);", (id, horario_entrada, horario_salida, estado))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()
    
    #ELIMINAR
    @classmethod
    def eliminar(cls, id):
        conexion = bd.Conexion()

        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_ELIMINAR_HORARIO(%s);", (id, ))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()

    #DAR DE BAJA
    @classmethod
    def darBaja(cls, id):
        conexion = bd.Conexion()
        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_DARBAJA_HORARIO(%s);", (id, ))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            print(resultado)
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()