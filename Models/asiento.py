import bd

class Asiento:
    def __init__(self, id=None, nro_asiento=None, id_nivel=None, tipo_asiento=None, estado=None,
                 fecha_registro=None, usuario=None):
        self.id = id
        self.nro_asiento = nro_asiento
        self.id_nivel = id_nivel
        self.tipo_asiento = tipo_asiento
        self.estado = estado
        self.fecha_registro = fecha_registro
        self.usuario = usuario
    
    @classmethod
    def verificarSolapamiento(cls,X1,Y1,X2,Y2):
        X1 = int(X1)
        X2 = int(X2)
        Y1 = int(Y1)
        Y2 = int(Y2)
        if X1 >= Y1 or X2 >= Y2:
            return False
        
        if X1 < Y2 and X2 < Y1:
            return True
        else:
            return False

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
    
    @classmethod
    def obtenerDatosAsiento(cls,id):
        conexion = bd.Conexion()
        try:
            datos =conexion.obtener("""
                SELECT 
                    v.id AS id_viaje, 
                    e_origen.nro_orden AS orden_origen,
                    e_destino.nro_orden AS orden_destino 
                FROM detalle_viaje dv INNER JOIN detalle_viaje_asiento dva ON dv.id = dva.idDetalle_Viaje
                INNER JOIN viaje v ON dv.idViaje = v.id
                INNER JOIN ruta r ON r.id = v.idRuta
                INNER JOIN sucursal s_origen ON dv.idSucursalOrigen = s_origen.id
                INNER JOIN sucursal s_destino ON dv.idSucursalDestino = s_destino.id
                INNER JOIN escala e_origen ON r.id = e_origen.idRuta AND s_origen.id = e_origen.idSucursal
                INNER JOIN escala e_destino ON r.id = e_destino.idRuta AND s_destino.id = e_destino.idSucursal
                WHERE dva.id = %s
                             """,(id,))
            datos_generales_asiento = datos[0]
            print(5)
            return datos_generales_asiento
        except Exception as e:
            return None
    
    @classmethod
    def actualizarEstadoAsiento(cls,id,estado):
        conexion = bd.Conexion()
        try:
            datosAsiento = Asiento.obtenerDatosAsiento(id)
            print(1)
            id_viaje = datosAsiento.get("id_viaje")
            orden_origen = datosAsiento.get("orden_origen")
            orden_destino = datosAsiento.get("orden_destino")
            print(2)
            listita = conexion.obtener("""
                SELECT 
                    dva.id AS id_asiento,
                    e_origen.nro_orden AS orden_origen,
                    e_destino.nro_orden AS orden_destino 
                FROM detalle_viaje dv INNER JOIN detalle_viaje_asiento dva ON dv.id = dva.idDetalle_Viaje
                INNER JOIN asiento a ON a.id = dva.idAsiento
                INNER JOIN viaje v ON dv.idViaje = v.id
                INNER JOIN ruta r ON r.id = v.idRuta
                INNER JOIN sucursal s_origen ON dv.idSucursalOrigen = s_origen.id
                INNER JOIN sucursal s_destino ON dv.idSucursalDestino = s_destino.id
                INNER JOIN escala e_origen ON r.id = e_origen.idRuta AND s_origen.id = e_origen.idSucursal
                INNER JOIN escala e_destino ON r.id = e_destino.idRuta AND s_destino.id = e_destino.idSucursal
                WHERE v.id = %s AND a.id = (SELECT idAsiento FROM detalle_viaje_asiento WHERE id = %s)
            """, (id_viaje,id))
            print(3)
            for dic_asientos in listita:
                banderita = Asiento.verificarSolapamiento(dic_asientos.get("orden_origen"),dic_asientos.get("orden_destino"), orden_origen,orden_destino)
                print(banderita)
                if (banderita): conexion.ejecutar("UPDATE detalle_viaje_asiento SET esDisponible = %s WHERE id = %s",(estado,dic_asientos.get("id_asiento")))
            print(4)
        finally:
            conexion.cerrar()

    @classmethod
    def ocupar_asiento(cls, id):
        Asiento.actualizarEstadoAsiento(id,0)            
    @classmethod
    def liberar_asiento(cls, id):
        Asiento.actualizarEstadoAsiento(id,1)

            
    @classmethod
    def obtener_estado(cls, id):
        conexion = bd.Conexion()
        try:
            lista = conexion.obtener("SELECT esDisponible as estado FROM detalle_viaje_asiento where id = %s;", (id,))
            return lista[0]
        finally:
            conexion.cerrar()
