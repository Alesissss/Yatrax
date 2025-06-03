import bd

class PreguntasFrecuentes:
    def __init__(self, id=None, pregunta=None, respuesta=None, estado=None, fecha_registro=None, usuario=None):
        self.id = id
        self.pregunta = pregunta
        self.respuesta = respuesta
        self.estado = estado
        self.fecha_registro = fecha_registro
        self.usuario = usuario
    
    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            return conexion.obtener("SELECT id, pregunta, respuesta, estado, fecha_registro, usuario FROM preguntas_frecuentes")
        finally:
            conexion.cerrar()
            
    @classmethod
    def obtener_por_id(cls, id):
        conexion = bd.Conexion()
        try:
            return conexion.obtener("SELECT id, pregunta, respuesta, estado, fecha_registro, usuario FROM preguntas_frecuentes WHERE  id = %s", (id,))
        finally:
            conexion.cerrar()
            
    @classmethod
    def registrar(cls, pregunta, respuesta, estado, usuario):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar(
                "CALL SP_REGISTRAR_PREGUNTA_FRECUENTE(%s, %s, %s, %s)",
                (pregunta, respuesta, estado, usuario)
            )
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()
            
    @classmethod
    def editar(cls, id, pregunta, respuesta, estado, usuario):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar(
                "CALL SP_EDITAR_PREGUNTA_FRECUENTE(%s, %s, %s, %s, %s)",
                (id, pregunta, respuesta, estado, usuario)
            )
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()
            
    @classmethod
    def eliminar(cls, id):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_ELIMINAR_PREGUNTA_FRECUENTE(%s)", (id,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()
            
    @classmethod
    def dar_baja(cls, id):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_DAR_BAJA_PREGUNTA_FRECUENTE(%s)", (id,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()