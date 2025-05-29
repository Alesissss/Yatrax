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
            viajes = conexion.obtener(""" SELECT v.id, v.idRuta, r.nombre, tv.id_servicio, s.nombre, ve.placa, v.esReprogramado, v.esPostergado, v.fecha_salida_estimada, v.fecha_llegada_estimada
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
            viaje = conexion.obtener(""" SELECT v.id, v.idRuta, r.nombre, tv.id_servicio, s.nombre, ve.placa, v.esReprogramado, v.esPostergado, v.fecha_salida_estimada, v.fecha_llegada_estimada FROM viaje v
                INNER JOIN ruta r on v.idRuta = r.id
                INNER JOIN vehiculo ve on ve.id = v.idVehiculo
                INNER JOIN estado_viaje ev on v.estadoViaje = ev.id
                INNER JOIN tipo_vehiculo tv on tv.id = ve.id_tipo_vehiculo
                INNER JOIN servicio s on s.id = tv.id_servicio WHERE r.id = %s""", (viaje_id,))
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
    def registrar(cls, nombre, estado, tipo, escalas, usuario):
        try:
            conexion = bd.Conexion()

            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_REGISTRAR_RUTA(%s, %s, %s, %s);", (nombre, estado, tipo, usuario), auto_commit=False)

            # Obtener el mensaje de error y el último idRuta generado
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2, LAST_INSERT_ID() AS idRuta;")
            idRuta = resultado[0]['idRuta']  # Obtener el último ID generado por la ruta
            msj2 = resultado[0]['@MSJ2']

            if msj2:  # Si hay un mensaje de error en msj2
                raise Exception('Error al registrar ruta: ' + msj2)

            # Insertar las escalas
            for escala in escalas:
                conexion.ejecutar("INSERT INTO escala (nro_orden, idSucursal, idRuta, usuario) VALUES (%s, %s, %s, %s)",
                                (escala['nroOrden'], escala['id'], idRuta, usuario), auto_commit=False)

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
    def obtenerOrigenes():
        conexion = bd.Conexion()
        try:
            lista_origenes = conexion.obtener("""
                SELECT s.id, s.ciudad AS ciudad
                FROM viaje v INNER JOIN ruta r on v.idRuta = r.id
                INNER JOIN escala e on e.idRuta = r.id
                INNER JOIN sucursal s on s.id = e.idSucursal
                WHERE e.nro_orden = 1
            """                 
            )
            return lista_origenes
        finally:
            conexion.cerrar()
    def obtenerDestinosPorOrigen(id):
        conexion = bd.Conexion()
        try:
            lista_origenes = conexion.obtener("""
                SELECT s.id, s.ciudad AS ciudad
                FROM viaje v INNER JOIN ruta r on v.idRuta = r.id
                INNER JOIN escala e on e.idRuta = r.id
                INNER JOIN sucursal s on s.id = e.idSucursal
                WHERE e.nro_orden = 1
            """                 
            )
            return lista_origenes
        finally:
            conexion.cerrar()

