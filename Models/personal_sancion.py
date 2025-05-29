import bd
import hashlib

class Personal_Sancion:
    def __init__(self, personalid = None, incidenciaid = None, descripcion = None, fecha_fin = None, estado = None, fecha_registro = None, usuario = None):
        self.personalid = personalid
        self.incidenciaid = incidenciaid
        self.descripcion = descripcion
        self.fecha_fin = fecha_fin
        self.estado = estado
        self.fechaRegistro = fecha_registro
        self.usuario = usuario

    @classmethod
    def obtener_todos(cls):
        try:
            conexion = bd.Conexion()
            personal_sancion = conexion.obtener("""
                        SELECT pr.nombre as PERSONAL, ic.nombre as SANCIÓN, pr_ic.descripcion, pr_ic.fecha_fin, pr_ic.estado
                        from personal_incidencia pr_ic INNER JOIN personal pr ON pr_ic.personalid = pr.id
                        INNER JOIN incidencia ic ON pr_ic.incidenciaid = ic.id
                                       """)
            return personal_sancion
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, personalid, incidenciaid):
        try:
            conexion = bd.Conexion()
            personal_sancion = conexion.obtener("SELECT pr.nombre as PERSONAL, ic.nombre as SANCIÓN, pr_ic.descripcion, pr_ic.fecha_fin, pr_ic.estado from personal_incidencia pr_ic INNER JOIN personal pr ON pr_ic.personalid = pr.id INNER JOIN incidencia ic ON pr_ic.incidenciaid = ic.id WHERE personalid = %s AND incidenciaid = %s", (personalid, incidenciaid,))
            return personal_sancion[0] if personal_sancion else None
        finally:
                conexion.cerrar()

    @classmethod
    def eliminar_sancion(cls, incidenciaid, personalid):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_ELIMINAR_PERSONAL_INCIDENCIA(%s, %s);", (incidenciaid, personalid,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()
    
    @classmethod
    def registrar(cls, nombre, descripcion, duracion_sancion, estado, usuario):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_REGISTRAR_INCIDENCIA(%s, %s, %s, %s, %s);", (nombre, descripcion, duracion_sancion, estado, usuario))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()

    @classmethod
    def editar(cls, personalid, incidenciaid, descripcion, estado):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_EDITAR_PERSONAL_INCIDENCIA(%s, %s, %s, %s)", (personalid, incidenciaid, descripcion, estado))
            resultado = conexion.obtener("SELECT @MSJ, @MS2J;")
            return resultado[0]
        finally:
            conexion.cerrar()
    
    @classmethod
    def darBaja(cls, incidenciaid, personalid):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_DARBAJA_PERSONAL_INCIDENCIA(%s, %s)", (incidenciaid, personalid,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()
            