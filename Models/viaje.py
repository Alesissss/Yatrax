import bd

class Viaje:
    def __init__(self, id=None, idRuta=None, idVehiculo=None, estado=None, estadoViaje=None, esReprogramado=None, esPostergado=None, fechaSalidaEstimada=None, fechaSalidaReal=None, fechaLlegadaEstimada=None, fechaLlegadaReal=None, fechaRegistro=None, usuario=None):
        self.id = id
        self.idRuta = idRuta
        self.idVehiculo = idVehiculo
        self.estado = estado
        self.estadoViaje = estadoViaje
        self.esReprogramado = esReprogramado
        self.esPostergado = esPostergado
        self.fechaSalidaEstimada = fechaSalidaEstimada
        self.fechaSalidaReal = fechaSalidaReal
        self.fechaLlegadaEstimada = fechaLlegadaEstimada
        self.fechaLlegadaReal = fechaLlegadaReal
        #Auditoría
        self.fechaRegistro = fechaRegistro
        self.usuario = usuario

    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            viajes = conexion.obtener(""" SELECT v.id, v.idRuta, v.estado, v.estadoViaje AS idEstadoViaje, ev.nombre AS estado_viaje, r.nombre AS ruta, 
                r.tipo AS tipo_ruta, tv.id_servicio, s.nombre AS servicio, CONCAT(tv.nombre, ' - ', ve.placa) AS vehiculo, 
                v.esReprogramado, v.esPostergado, v.fecha_salida_estimada, v.fecha_llegada_estimada
                FROM viaje v
                INNER JOIN ruta r on v.idRuta = r.id
                INNER JOIN vehiculo ve on ve.id = v.idVehiculo
                INNER JOIN estado_viaje ev on v.estadoViaje = ev.id
                INNER JOIN tipo_vehiculo tv on tv.id = ve.id_tipo_vehiculo
                INNER JOIN servicio s on s.id = tv.id_servicio;
            """)
            return viajes
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, viaje_id):
        conexion = bd.Conexion()
        try:
            viaje = conexion.obtener(""" SELECT v.id, v.idRuta, v.estado, v.estadoViaje AS idEstadoViaje, ev.nombre AS estado_viaje, r.nombre AS ruta, 
                r.tipo AS tipo_ruta, tv.id_servicio, s.nombre AS servicio, CONCAT(tv.nombre, ' - ', ve.placa) AS vehiculo, 
                v.esReprogramado, v.esPostergado, v.fecha_salida_estimada, v.fecha_llegada_estimada
                FROM viaje v
                INNER JOIN ruta r on v.idRuta = r.id
                INNER JOIN vehiculo ve on ve.id = v.idVehiculo
                INNER JOIN estado_viaje ev on v.estadoViaje = ev.id
                INNER JOIN tipo_vehiculo tv on tv.id = ve.id_tipo_vehiculo
                INNER JOIN servicio s on s.id = tv.id_servicio;
                WHERE r.id = %s""", (viaje_id,))
            return viaje[0] if viaje else None
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_escalas_por_ruta(cls, ruta_id):
        conexion = bd.Conexion()
        try:
            escalas = conexion.obtener(""" SELECT id, nro_orden, idSucursal, idRuta from escala WHERE idRuta = %s ORDER BY nro_orden""", (ruta_id,))
            return escalas
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_personal_viaje(cls, viaje_id):
        try:
            conexion = bd.Conexion()
            personal = conexion.obtener(""" SELECT dp.idPersonal, p.nombre, tp.nombre
                FROM detalle_personal dp
                INNER JOIN personal p on dp.idPersonal = p.id
                INNER JOIN tipo_personal tp on tp.id = dp.idTipoPersonal WHERE dp.idViaje = %s;""", (viaje_id,))
            return personal
        finally:
            conexion.cerrar()
    # REGISTRAR
    @classmethod
    def registrar(cls, idRuta, idVehiculo, estado, fecha_salida_estimada, fecha_llegada_estimada, detalles_viajes, choferes, tripulantes, usuario):
        try:
            conexion = bd.Conexion()

            conexion.ejecutar(""" INSERT INTO viaje (idRuta, idVehiculo, estado, idEstadoViaje, esReprogramado, fechaHoraSalida, fechaHoraLlegada, usuario) VALUES (%s, %s, %s, 1, 0, %s, %s, %s) """, (idRuta, idVehiculo, estado, fecha_salida_estimada, fecha_llegada_estimada, usuario), auto_commit=False)

            resultado = conexion.obtener("SELECT LAST_INSERT_ID() AS idViaje;")
            idViaje = resultado[0]['idViaje'] 

            # Insertar los itinerarios
            for detalle in detalles_viajes:
                conexion.ejecutar("INSERT INTO detalle_viaje (idViaje, idSucursalOrigen, idSucursalDestino, precio, fechaSalida, fechaLlegadaEstimada, usuario) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                                  (idViaje, detalle['id_sucursal_origen'], detalle['id_sucursal_destino'], detalle['precio'], detalle['fecha_salida'], detalle['fecha_llegada'], usuario), auto_commit=False)

            # Insertar los choferes
            for chofer in choferes:
                conexion.ejecutar("INSERT INTO detalle_personal (idPersonal, idTipoPersonal, idViaje, usuario) VALUES (%s, %s, %s, %s)",
                                (chofer['id'], chofer['id_tipopersonal'], idViaje, usuario), auto_commit=False)
            
            # Insertar los tripulantes
            for tripulante in tripulantes:
                conexion.ejecutar("INSERT INTO detalle_personal (idPersonal, idTipoPersonal, idViaje, usuario) VALUES (%s, %s, %s, %s)",
                                (tripulante['id'], tripulante['id_tipopersonal'], idViaje, usuario), auto_commit=False)

            # Si todo es correcto, confirmamos la transacción
            conexion.conn.commit()
            return {'@MSJ': 'Se programó el viaje correctamente', '@MSJ2': ''}  # Retorna un diccionario con los mensajes

        except Exception as e:
            # Si algo falla, hacemos un rollback
            conexion.conn.rollback()
            return {'@MSJ': '', '@MSJ2': f'Error al ejecutar la transacción de registro de viaje: {repr(e)}'}

        finally:
            # Cerramos la conexión
            conexion.cerrar()

    #EDITAR
    @classmethod
    def editar(cls, id, nombre, tipo, estado, escalas, usuario):
        try:
            conexion = bd.Conexion()
            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_EDITAR_RUTA(%s, %s, %s, %s);", (id, nombre, tipo, estado), auto_commit=False)

            # Obtener el mensaje de error y el último idRuta generado
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            msj2 = resultado[0]['@MSJ2']

            if msj2:  # Si hay un mensaje de error en msj2
                raise Exception('Error al editar ruta: ' + msj2)

            escalas_actuales = conexion.obtener(""" SELECT id, nro_orden, idSucursal, idRuta from escala WHERE idRuta = %s""", (id,))

            # Borrar las escalas que existen actualmente
            conexion.ejecutar("DELETE FROM escala WHERE idRuta = %s", (id), auto_commit=False)

            # Insertar las escalas
            for escala in escalas:
                conexion.ejecutar("INSERT INTO escala (nro_orden, idSucursal, idRuta, usuario) VALUES (%s, %s, %s, %s)",
                                (escala['nroOrden'], escala['id'], id, usuario), auto_commit=False)

            # Si todo es correcto, confirmamos la transacción
            conexion.conn.commit()
            return resultado[0]  # Retorna un diccionario con los mensajes

        except Exception as e:
            # Si algo falla, hacemos un rollback
            conexion.conn.rollback()
            return {'@MSJ': '', '@MSJ2': f'Error al ejecutar la transacción de registro de ruta: {repr(e)}'}

        finally:
            # Cerramos la conexión
            conexion.cerrar()

    #ELIMINAR
    @classmethod
    def eliminar(cls, id):
        conexion = bd.Conexion()

        try:
            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_ELIMINAR_RUTA(%s);", (id, ))

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
            conexion.ejecutar("CALL SP_DARBAJA_RUTA(%s);", (id, ))

            # Obtener mensajes de salida
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]  # Retorna un diccionario con los mensajes
        finally:
            conexion.cerrar()
    

    @classmethod
    def obtenerDestinos(cls):
        conexion = bd.Conexion()
        try:
            lista_origenes = conexion.obtener(f"""
                SELECT DISTINCT CONCAT(s_origen.ciudad,' - ',s_destino.ciudad) as ruta
                FROM detalle_viaje dv INNER JOIN escala e_origen ON dv.idSucursalOrigen = e_origen.id
                INNER JOIN sucursal s_origen ON s_origen.id = e_origen.id
                INNER JOIN escala e_destino ON dv.idSucursalDestino = e_destino.id
                INNER JOIN sucursal s_destino ON s_destino.id = e_destino.id
                INNER JOIN viaje v ON v.id = dv.idViaje
                WHERE v.id = 1;
            """                 
            )
            return lista_origenes
        finally:
            conexion.cerrar()
    
    @classmethod
    def buscarViajePorRutaYFecha(cls, origen,destino,fecha):
        conexion = bd.Conexion()
        try:
            datos_viaje = conexion.obtener("""
            SELECT 
            dv.id,
            DATE_FORMAT(dv.fechaSalida,'%%H:%%i') as hora_salida,
            DATE_FORMAT(dv.fechaLlegadaEstimada, '%%H:%%i') as hora_llegada,
            s_origen.ciudad AS ciudad_origen,
            s_destino.ciudad AS ciudad_destino,
            s_origen.nombre AS sucursal_origen,
            s_destino.nombre AS sucursal_destino,
            se.nombre as servicio,
            ve.id AS id_vehículo,
            CASE 
                WHEN e_destino.nro_orden - e_origen.nro_orden = 1 THEN 'Directo'
                ELSE 'Escala'
            END as tipo
            FROM detalle_viaje dv INNER JOIN sucursal s_origen ON dv.idSucursalOrigen = s_origen.id
            INNER JOIN sucursal s_destino ON dv.idSucursalDestino = s_destino.id
            INNER JOIN viaje vi ON dv.idViaje = vi.id
            INNER JOIN vehiculo ve ON ve.id = vi.idVehiculo
            INNER JOIN tipo_vehiculo tv ON tv.id = ve.id_tipo_vehiculo
            INNER JOIN servicio se ON se.id = tv.id_servicio
            INNER JOIN ruta r ON r.id = vi.idRuta
            INNER JOIN escala e_origen ON r.id = e_origen.idRuta AND s_origen.id = e_origen.idSucursal
            INNER JOIN escala e_destino ON r.id = e_destino.idRuta AND s_destino.id = e_destino.idSucursal
            WHERE s_origen.ciudad = %s AND s_destino.ciudad = %s AND DATE(dv.fechaSalida) = %s;

                             """, (origen,destino,fecha))
            return datos_viaje
        finally:
            conexion.cerrar()
    @classmethod
    def obtener_tipo_vehiculo_por_dv(cls,id_viaje):
        conexion = bd.Conexion()
        try:
            id = conexion.obtener("""
                SELECT tv.id as id_tipo_vehiculo
                FROM detalle_viaje dv INNER JOIN viaje v ON v.id = dv.idViaje
                INNER JOIN vehiculo ve ON ve.id = v.idVehiculo
                INNER JOIN tipo_vehiculo tv ON tv.id = ve.id_tipo_vehiculo
                WHERE dv.id = %s
                                  """,(id_viaje,))
            return id[0]
        finally:
            conexion.cerrar()
