import bd

class Promocion:
    def __init__(self, id=None, nombre=None, estado=None, fecha_inicio=None, fecha_fin=None, codigo=None, monto_promo=None):
        self.id = id
        self.nombre = nombre
        self.estado = estado
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.codigo = codigo
        self.monto_promo = monto_promo

    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            return conexion.obtener("""
                SELECT id, nombre, estado, fecha_inicio, fecha_fin, codigo, monto_promo 
                FROM promocion
            """)
        finally:
            conexion.cerrar()
            
    @classmethod
    def obtener_todos_activos(cls):
        conexion = bd.Conexion()
        try:
            return conexion.obtener("""
                SELECT id, nombre, estado, fecha_inicio, fecha_fin, codigo, monto_promo , CURDATE()
                FROM promocion
                where estado = 1 and
                fecha_fin >= CURDATE() AND
                fecha_inicio <= CURDATE()
            """)
        finally:
            conexion.cerrar()
    
    def validarExistencia(cls,codigo):
        

    @classmethod
    def obtener_por_id(cls, id):
        conexion = bd.Conexion()
        try:
            resultado = conexion.obtener("""
                SELECT id, nombre, estado, fecha_inicio, fecha_fin, codigo, monto_promo 
                FROM promocion 
                WHERE id = %s
            """, (id,))
            return resultado[0] if resultado else None
        finally:
            conexion.cerrar()

    @classmethod
    def registrar(cls, nombre, estado, fecha_inicio, fecha_fin, codigo, monto_promo):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar(
                "CALL SP_REGISTRAR_PROMOCION(%s, %s, %s, %s, %s, %s)",
                (nombre, estado, fecha_inicio, fecha_fin, codigo, monto_promo)
            )
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()

    @classmethod
    def editar(cls, id, nombre, estado, fecha_inicio, fecha_fin, codigo, monto_promo):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar(
                "CALL SP_EDITAR_PROMOCION(%s, %s, %s, %s, %s, %s, %s)",
                (id, nombre, estado, fecha_inicio, fecha_fin, codigo, monto_promo)
            )
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()

    @classmethod
    def eliminar(cls, id):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_ELIMINAR_PROMOCION(%s)", (id,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()

    @classmethod
    def dar_baja(cls, id):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_DAR_BAJA_PROMOCION(%s)", (id,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_codigo(cls, cod):
        conexion = bd.Conexion()
        try:
            resultado = conexion.obtener("""
                SELECT id FROM promocion WHERE codigo = %s
            """, (cod,))
            return resultado[0]["id"] if resultado else None
        finally:
            conexion.cerrar()