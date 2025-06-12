import bd

class Asiento:
    def __init__(self, id=None, nro_asiento=None, id_nivel=None, tipo_asiento=None, estado=None,
                 fecha_registro=None, usuario=None, estadoProceso=None, estadoRegistro=None):
        self.id = id
        self.nro_asiento = nro_asiento
        self.id_nivel = id_nivel
        self.tipo_asiento = tipo_asiento
        self.estado = estado
        self.fecha_registro = fecha_registro
        self.usuario = usuario
        # Auditoría
        self.estadoProceso = estadoProceso
        self.estadoRegistro = estadoRegistro

    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            asientos = conexion.obtener("""
                SELECT a.id AS id, a.nombre AS nombre, v.placa AS vehiculo ,n.nroPiso AS piso,h.nombre as tipo_asiento, a.estado AS estado
                FROM asiento a inner join vehiculo v on a.id_vehiculo = v.id
                inner join nivel_herramienta nh on nh.id = a.id_nivel_herramienta
                inner join nivel n on n.id = nh.id_nivel
                inner join herramienta h on h.id = nh.id_herramienta;
            """)
            return asientos
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, asiento_id):
        conexion = bd.Conexion()
        try:
            asiento = conexion.obtener("""
                SELECT a.id, a.nro_asiento, n.nroPiso AS nivel, a.tipo_asiento, a.estado 
                FROM asiento a INNER JOIN nivel n ON a.id_nivel = n.id
                WHERE a.id = %s
            """, (asiento_id,))
            return asiento[0] if asiento else None
        finally:
            conexion.cerrar()
            
    @classmethod
    def obtener_por_id_vehiculo(cls, vehiculo_id):
        conexion = bd.Conexion()
        try:
            asientos = conexion.obtener(""" SELECT a.id, a.nombre, a.estado 
                FROM asiento a 
                INNER JOIN nivel_herramienta nh ON a.id_nivel_herramienta = nh.id 
                INNER JOIN herramienta h ON h.id = nh.id_herramienta
                INNER JOIN tipo_herramienta th ON th.id = h.id_tipo
                WHERE th.id = 1 AND a.id_vehiculo = %s """, (vehiculo_id,))
            return asientos
        finally:
            conexion.cerrar()

    @classmethod
    def registrar(cls, nro_asiento, id_nivel, tipo_asiento, estado, usuario):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_REGISTRAR_ASIENTO(%s, %s, %s, %s, %s);", (nro_asiento, id_nivel, tipo_asiento, estado, usuario))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()

    @classmethod
    def editar(cls, id, nro_asiento, id_nivel, tipo_asiento, estado,usuario):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_EDITAR_ASIENTO(%s, %s, %s, %s, %s,%s);", (id, nro_asiento, id_nivel, tipo_asiento, estado,usuario))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()

    @classmethod
    def eliminar(cls, id):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_ELIMINAR_ASIENTO(%s);", (id,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()

    @classmethod
    def dar_baja(cls, id):
        conexion = bd.Conexion()
        try:
            conexion.ejecutar("CALL SP_DARBAJA_ASIENTO(%s);", (id,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            conexion.cerrar()
