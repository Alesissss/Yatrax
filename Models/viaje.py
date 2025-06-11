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

            conexion.ejecutar(""" INSERT INTO viaje (idRuta, idVehiculo, estado, estadoViaje, esReprogramado, fechaHoraSalida, fechaHoraLlegada, usuario) VALUES (%s, %s, %s, 1, 0, %s, %s, %s) """, (idRuta, idVehiculo, estado, fecha_salida_estimada, fecha_llegada_estimada, usuario), auto_commit=False)

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
                SELECT DISTINCT CONCAT(s_origen.ciudad,'-',s_destino.ciudad) as ruta
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
                datos_viaje.hora_salida,
                datos_viaje.hora_llegada,
                datos_viaje.sucursal_salida,
                datos_viaje.sucursal_llegada,
                datos_viaje.ciudad_salida,
                datos_viaje.ciudad_llegada,
                datos_viaje.tipo_viaje,
                datos_viaje.servicio,
                GROUP_CONCAT(
                    CONCAT('Piso ', info_asientos.nroPiso, ': ', info_asientos.cantidad, ' asientos disponibles')
                    ORDER BY info_asientos.nroPiso SEPARATOR ' | '
                ) AS niveles_con_asientos

            FROM (
                SELECT 
                    v.id AS id_viaje,
                    DATE_FORMAT(v.fecha_salida_estimada, "%%H:%%i") AS hora_salida,
                    DATE_FORMAT(v.fecha_llegada_estimada, "%%H:%%i") AS hora_llegada,
                    s_origen.nombre AS sucursal_salida,
                    s_destino.nombre AS sucursal_llegada,
                    s_origen.ciudad AS ciudad_salida,
                    s_destino.ciudad AS ciudad_llegada,
                    IF(e_intermedias.total_escalas > 0, 'Escala', 'Directo') AS tipo_viaje,
                    se.nombre AS servicio
                FROM viaje v
                INNER JOIN ruta r ON v.idRuta = r.id
                INNER JOIN escala e_salida ON e_salida.idRuta = r.id AND e_salida.nro_orden = 1
                INNER JOIN sucursal s_origen ON s_origen.id = e_salida.idSucursal
                INNER JOIN (
                    SELECT idRuta, MAX(nro_orden) AS max_orden
                    FROM escala GROUP BY idRuta
                ) e_max ON e_max.idRuta = r.id
                INNER JOIN escala e_llegada ON e_llegada.idRuta = r.id AND e_llegada.nro_orden = e_max.max_orden
                INNER JOIN sucursal s_destino ON s_destino.id = e_llegada.idSucursal
                INNER JOIN vehiculo ve ON ve.id = v.idVehiculo
                INNER JOIN tipo_vehiculo tv ON tv.id = ve.id_tipo_vehiculo
                INNER JOIN servicio se ON se.id = tv.id_servicio
                LEFT JOIN (
                    SELECT idRuta, COUNT(*) AS total_escalas
                    FROM escala WHERE nro_orden > 1
                    GROUP BY idRuta
                ) e_intermedias ON e_intermedias.idRuta = r.id
                WHERE s_origen.ciudad = %s
                AND s_destino.ciudad = %s
                AND DATE(v.fecha_salida_estimada) = %s
            ) AS datos_viaje

            LEFT JOIN (
                SELECT 
                    v.id AS id_viaje,
                    n.nroPiso,
                    COUNT(a.id) AS cantidad
                FROM viaje v
                INNER JOIN vehiculo ve ON ve.id = v.idVehiculo
                INNER JOIN tipo_vehiculo tv ON tv.id = ve.id_tipo_vehiculo
                INNER JOIN nivel n ON n.id_tipo_vehiculo = tv.id
                INNER JOIN asiento a ON a.id_vehiculo = v.id AND a.estado = 1
                GROUP BY v.id, n.nroPiso
            ) AS info_asientos ON info_asientos.id_viaje = datos_viaje.id_viaje

            GROUP BY datos_viaje.id_viaje;

                             """, (origen,destino,fecha))
            return datos_viaje
        finally:
            conexion.cerrar()

