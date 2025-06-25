from datetime import datetime
from decimal import Decimal

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
            viajes = conexion.obtener(""" SELECT v.id, v.idRuta, v.estado, v.idEstadoViaje, ev.nombre AS estado_viaje, r.nombre AS ruta, 
                r.tipo AS tipo_ruta, tv.id_servicio, s.nombre AS servicio, CONCAT(tv.nombre, ' - ', ve.placa) AS vehiculo, 
                v.esReprogramado, v.fechaHoraSalida, v.fechaHoraLlegada
                FROM viaje v
                INNER JOIN ruta r on v.idRuta = r.id
                INNER JOIN vehiculo ve on ve.id = v.idVehiculo
                INNER JOIN estado_viaje ev on v.idEstadoViaje = ev.id
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
            viaje = conexion.obtener(""" SELECT v.id, v.idRuta, v.estado, v.idEstadoViaje, ev.nombre AS estado_viaje, r.nombre AS ruta, 
                r.tipo AS tipo_ruta, tv.id_servicio, s.nombre AS servicio, CONCAT(tv.nombre, ' - ', ve.placa) AS vehiculo, 
                v.esReprogramado, v.fechaHoraSalida, v.fechaHoraLlegada
                FROM viaje v
                INNER JOIN ruta r on v.idRuta = r.id
                INNER JOIN vehiculo ve on ve.id = v.idVehiculo
                INNER JOIN estado_viaje ev on v.idEstadoViaje = ev.id
                INNER JOIN tipo_vehiculo tv on tv.id = ve.id_tipo_vehiculo
                INNER JOIN servicio s on s.id = tv.id_servicio
                WHERE r.id = %s""", (viaje_id,))
            return viaje[0] if viaje else None
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_viaje(cls, idViaje):
        try:
            conexion = bd.Conexion()
            
            viaje = conexion.obtener("""SELECT * FROM viaje WHERE id = %s""", (idViaje,))
            
            detalles_viaje = conexion.obtener("""SELECT * FROM detalle_viaje WHERE idViaje = %s""", (idViaje,))
            
            personal = conexion.obtener("""SELECT * FROM detalle_personal WHERE idViaje = %s""", (idViaje,))
            
            # Obtener escalas para la ruta
            escalas = []
            if viaje:
                escalas = conexion.obtener("""SELECT es.id, es.nro_orden, es.idSucursal, es.distancia_estimada, es.tiempo_estimado, CONCAT(UPPER(suc.ciudad), '-', suc.nombre) AS nombre, es.idRuta from escala es INNER JOIN sucursal suc on es.idSucursal = suc.id WHERE idRuta = %s ORDER BY nro_orden""", (viaje[0]['idRuta'],))

            return {
                "viaje": viaje[0] if viaje else None,
                "detalles_viaje": detalles_viaje,
                "personal": personal,
                "escalas": escalas
            }
        except Exception as e:
            print(f"Error al obtener datos del viaje: {repr(e)}")
            return None
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_datos_viaje_tracking(cls, idViaje):
        try:
            conexion = bd.Conexion()
            
            viaje = conexion.obtener("""SELECT v.id, v.idRuta, v.estado, v.idEstadoViaje, ev.nombre AS estado_viaje, r.nombre AS ruta, 
                r.tipo AS tipo_ruta, tv.id_servicio, s.nombre AS servicio, v.idVehiculo, CONCAT(tv.nombre, ' - ', ve.placa) AS vehiculo, 
                v.esReprogramado, v.fechaHoraSalida, v.fechaHoraLlegada
                FROM viaje v
                INNER JOIN ruta r on v.idRuta = r.id
                INNER JOIN vehiculo ve on ve.id = v.idVehiculo
                INNER JOIN estado_viaje ev on v.idEstadoViaje = ev.id
                INNER JOIN tipo_vehiculo tv on tv.id = ve.id_tipo_vehiculo
                INNER JOIN servicio s on s.id = tv.id_servicio
                WHERE v.id = %s""", (idViaje,))
            
            # Obtener escalas para la ruta
            escalas = []
            if viaje:
                escalas = conexion.obtener("""SELECT es.id, es.nro_orden, es.idSucursal, es.distancia_estimada, suc.latitud, suc.longitud,
                                           es.tiempo_estimado, CONCAT(UPPER(suc.ciudad), '-', suc.nombre) AS nombre, es.idRuta 
                                           FROM escala es 
                                           INNER JOIN sucursal suc on es.idSucursal = suc.id WHERE idRuta = %s 
                                           ORDER BY nro_orden""", (viaje[0]['idRuta'],))

            return {
                "viaje": viaje[0] if viaje else None,
                "escalas": escalas
            }
        except Exception as e:
            print(f"Error al obtener datos del viaje: {repr(e)}")
            return None
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
    def registrar(cls, idRuta, idVehiculo, estado, fecha_salida_estimada, fecha_llegada_estimada, detalles_viajes, choferes, tripulantes, asientos, usuario):
        try:
            conexion = bd.Conexion()

            conexion.ejecutar(""" INSERT INTO viaje (idRuta, idVehiculo, estado, idEstadoViaje, esReprogramado, fechaHoraSalida, fechaHoraLlegada, usuario) VALUES (%s, %s, %s, 1, 0, %s, %s, %s) """, (idRuta, idVehiculo, estado, fecha_salida_estimada, fecha_llegada_estimada, usuario), auto_commit=False)

            resultado = conexion.obtener("SELECT LAST_INSERT_ID() AS idViaje;")
            idViaje = resultado[0]['idViaje'] 

            # Insertar los itinerarios
            for detalle in detalles_viajes:
                conexion.ejecutar("INSERT INTO detalle_viaje (idViaje, idSucursalOrigen, idSucursalDestino, precio, fechaSalida, fechaLlegadaEstimada, usuario) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                                  (idViaje, detalle['id_sucursal_origen'], detalle['id_sucursal_destino'], detalle['precio'], detalle['fecha_salida'], detalle['fecha_llegada'], usuario), auto_commit=False)
                
                idDetalle_Viaje = conexion.obtener("SELECT LAST_INSERT_ID() AS idDetalle_Viaje;")
                idDetalle_Viaje = idDetalle_Viaje[0]['idDetalle_Viaje'] 

                # Insertar los asientos de subviajes
                for asiento in asientos:
                    conexion.ejecutar("INSERT INTO detalle_viaje_asiento (idDetalle_Viaje, idAsiento, usuario) VALUES (%s, %s, %s)", (idDetalle_Viaje, asiento['id'], usuario), auto_commit=False)

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
    def editar(cls, idViaje, idRuta, idVehiculo, estado, fechaHoraSalida, fechaHoraLlegada, detalles_viajes, choferes, tripulantes, asientos, usuario):
        try:
            conexion = bd.Conexion()

            # --- obtener flag de reprogramación y datos de itinerarios actuales y recibidos
            sePuedeReprogramar = bool(conexion.obtener(
                "SELECT 1 FROM conf_general WHERE viajesReprogramables = 1"
            ))

            # detectar si hay pasajes/asientos ocupados
            hay_pasajes = conexion.obtener(
                """ SELECT 1 FROM pasaje p
                    INNER JOIN detalle_viaje_asiento dva ON p.idDetalleViajeAsiento = dva.id
                    INNER JOIN detalle_viaje dv ON dva.idDetalle_Viaje = dv.id
                    WHERE dv.idViaje = %s LIMIT 1
                """,
                (idViaje,)
            )
            hay_asientos = conexion.obtener(
                """ SELECT 1 FROM detalle_viaje_asiento dva
                    WHERE dva.idDetalle_Viaje IN (
                        SELECT id FROM detalle_viaje WHERE idViaje = %s
                    )
                    AND dva.esDisponible = 0
                    LIMIT 1
                """,
                (idViaje,)
            )

            # --- rama de reprogramación
            if sePuedeReprogramar and (hay_pasajes or hay_asientos):
                # 0. Helpers
                def parse_front_fecha(fecha_str: str) -> datetime:
                    # ajusta el formato si es necesario
                    return datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")

                def to_map_act(lista):
                    # claves: (origen, destino, precio:Decimal)
                    return {
                        (d['idSucursalOrigen'],
                        d['idSucursalDestino'],
                        d['precio']): d
                        for d in lista
                    }

                def to_map_rec(lista):
                    # convierto precio a Decimal para que hashes+== cuadren
                    return {
                        (d['id_sucursal_origen'],
                        d['id_sucursal_destino'],
                        Decimal(d['precio'])): d
                        for d in lista
                    }

                # 1) cargo datos
                actuales = conexion.obtener(
                    """
                    SELECT idSucursalOrigen, idSucursalDestino, precio,
                        fechaSalida, fechaLlegadaEstimada
                    FROM detalle_viaje
                    WHERE idViaje = %s
                    """,
                    (idViaje,)
                )
                recibidos = detalles_viajes

                # 2) validaciones de número y rutas/precios
                if len(recibidos) != len(actuales):
                    raise Exception("No se puede reprogramar: cambió número de itinerarios.")

                map_act = to_map_act(actuales)
                map_rec = to_map_rec(recibidos)

                if set(map_act) != set(map_rec):
                    raise Exception("No se puede reprogramar: sólo cambian horarios, no rutas ni precios.")

                # 3) detectar cambio real de horario
                hubo_cambio = any(
                    parse_front_fecha(map_rec[key]['fecha_salida'])  != map_act[key]['fechaSalida']
                    or
                    parse_front_fecha(map_rec[key]['fecha_llegada']) != map_act[key]['fechaLlegadaEstimada']
                    for key in map_act
                )

                if not hubo_cambio:
                    # no hay nada que reprogramar: 
                    # salta esta rama y sigue con personal/bloqueo/edición completa
                    pass
                else:
                    # 4) actualizo horarios en detalle_viaje
                    for key, rec in map_rec.items():
                        orig, dest, precio = key
                        conexion.ejecutar(
                            """
                            UPDATE detalle_viaje
                            SET fechaSalida          = %s,
                                fechaLlegadaEstimada = %s,
                                usuario              = %s
                            WHERE idViaje            = %s
                            AND idSucursalOrigen    = %s
                            AND idSucursalDestino   = %s
                            AND precio              = %s
                            """,
                            (
                                parse_front_fecha(rec['fecha_salida']),
                                parse_front_fecha(rec['fecha_llegada']),
                                usuario,
                                idViaje,
                                orig,
                                dest,
                                precio,
                            ),
                            auto_commit=False
                        )

                    # 5. marcar viaje y fechas generales
                    conexion.ejecutar(
                        """
                        UPDATE viaje
                        SET idRuta          = %s,
                            idVehiculo      = %s,
                            estado          = %s,
                            fechaHoraSalida  = %s,
                            fechaHoraLlegada = %s,
                            esReprogramado   = 1
                        WHERE id = %s
                        """,
                        (idRuta, idVehiculo, estado, fechaHoraSalida, fechaHoraLlegada, idViaje),
                        auto_commit=False
                    )

                    # 6.1 Obtener los días adicionales a la reprogramación
                    dias_reprogramacion = conexion.obtener("SELECT max_dias_vigencia_reprogramacion FROM conf_general LIMIT 1")[0]['max_dias_vigencia_reprogramacion']

                    # 6.2. ejecutar el UPDATE en cadena
                    conexion.ejecutar("""
                        UPDATE pasaje p
                        JOIN detalle_viaje_asiento dva 
                        ON p.idDetalleViajeAsiento = dva.id
                        JOIN detalle_viaje dv 
                        ON dva.idDetalle_Viaje = dv.id
                        AND dv.idViaje = %s
                        SET
                        p.fechaReprogramacion = NOW()
                    """, (idViaje), auto_commit=False)

                    conexion.conn.commit()
                    return {'@MSJ': 'Viaje reprogramado correctamente', '@MSJ2': ''}

            # --- si no entra en reprogramación y tiene pasajes/u asientos, bloqueo normal
            if hay_pasajes or hay_asientos:
                # 1) obtener el personal actual
                personal_actual = conexion.obtener(
                    """
                    SELECT idPersonal, idTipoPersonal
                    FROM detalle_personal
                    WHERE idViaje = %s
                    """,
                    (idViaje,)
                )
                set_personal_actual = {(p['idPersonal'], p['idTipoPersonal']) for p in personal_actual}

                # 2) armar el set de lo que llegó (choferes + tripulantes)
                recibidos = choferes + tripulantes
                set_recibido = {(p['id'], p['id_tipopersonal']) for p in recibidos}

                # 3) comparar
                if set_personal_actual != set_recibido:
                    # hay cambios: actualizar sólo el personal
                    conexion.ejecutar(
                        "DELETE FROM detalle_personal WHERE idViaje = %s",
                        (idViaje,),
                        auto_commit=False
                    )
                    for p in recibidos:
                        conexion.ejecutar(
                            """
                            INSERT INTO detalle_personal
                                (idPersonal, idTipoPersonal, idViaje, usuario)
                            VALUES (%s, %s, %s, %s)
                            """,
                            (p['id'], p['id_tipopersonal'], idViaje, usuario),
                            auto_commit=False
                        )
                    conexion.conn.commit()
                    return {
                        '@MSJ': 'Personal del viaje actualizado correctamente',
                        '@MSJ2': ''
                    }
                # 4) si no hay cambios en personal, bloqueo normal
                raise Exception(
                    'El viaje no se puede modificar porque ya existen pasajes vendidos u ocupados, (Solo puede modificar el personal).'
                )

            # 1. Actualizar el viaje
            conexion.ejecutar("""
                UPDATE viaje
                SET idRuta = %s, idVehiculo = %s, estado = %s, fechaHoraSalida = %s, fechaHoraLlegada = %s
                WHERE id = %s
            """, (idRuta, idVehiculo, estado, fechaHoraSalida, fechaHoraLlegada, idViaje), auto_commit=False)

            conexion.ejecutar("DELETE FROM detalle_viaje_asiento WHERE idDetalle_Viaje IN (SELECT id FROM detalle_viaje WHERE idViaje = %s)", (idViaje,), auto_commit=False)
            conexion.ejecutar("DELETE FROM detalle_viaje WHERE idViaje = %s", (idViaje,), auto_commit=False)

            for detalle in detalles_viajes:
                conexion.ejecutar("""
                    INSERT INTO detalle_viaje (idViaje, idSucursalOrigen, idSucursalDestino, precio, fechaSalida, fechaLlegadaEstimada, usuario)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (idViaje, detalle['id_sucursal_origen'], detalle['id_sucursal_destino'], detalle['precio'], detalle['fecha_salida'], detalle['fecha_llegada'], usuario), auto_commit=False)

                idDetalle_Viaje = conexion.obtener("SELECT LAST_INSERT_ID() AS idDetalle_Viaje;")[0]['idDetalle_Viaje']
                for asiento in asientos:
                    conexion.ejecutar("""
                        INSERT INTO detalle_viaje_asiento (idDetalle_Viaje, idAsiento, usuario)
                        VALUES (%s, %s, %s)
                    """, (idDetalle_Viaje, asiento['id'], usuario), auto_commit=False)

            conexion.ejecutar("DELETE FROM detalle_personal WHERE idViaje = %s", (idViaje,), auto_commit=False)

            for chofer in choferes:
                conexion.ejecutar("""
                    INSERT INTO detalle_personal (idPersonal, idTipoPersonal, idViaje, usuario)
                    VALUES (%s, %s, %s, %s)
                """, (chofer['id'], chofer['id_tipopersonal'], idViaje, usuario), auto_commit=False)

            for tripulante in tripulantes:
                conexion.ejecutar("""
                    INSERT INTO detalle_personal (idPersonal, idTipoPersonal, idViaje, usuario)
                    VALUES (%s, %s, %s, %s)
                """, (tripulante['id'], tripulante['id_tipopersonal'], idViaje, usuario), auto_commit=False)

            conexion.conn.commit()
            return {'@MSJ': 'Viaje actualizado correctamente', '@MSJ2': ''}

        except Exception as e:
            conexion.conn.rollback()
            return {'@MSJ': '', '@MSJ2': f'Error al actualizar el viaje: {str(e)}'}

        finally:
            conexion.cerrar()

    #ELIMINAR
    @classmethod
    def eliminar(cls, id):
        try:
            conexion = bd.Conexion()

            result_pasaje = conexion.obtener(""" SELECT 1 FROM pasaje p 
                            INNER JOIN detalle_viaje_asiento dva ON p.idDetalleViajeAsiento = dva.id
                            INNER JOIN detalle_viaje dv ON dva.idDetalle_Viaje = dv.id
                            INNER JOIN viaje v ON dv.idViaje = v.id WHERE v.id = %s LIMIT 1""", (id,))
            
            result_asiento = conexion.obtener(""" SELECT 1 FROM detalle_viaje_asiento dva
                            INNER JOIN detalle_viaje dv ON dva.idDetalle_Viaje = dv.id
                            INNER JOIN viaje v ON dv.idViaje = v.id
                            WHERE dva.esDisponible = 0 AND v.id = %s LIMIT 1""", (id,))
            
            if result_pasaje or result_asiento:
                raise Exception('El viaje no se puede eliminar porque ya existen pasajes vendidos para los itinerarios.')

            conexion.ejecutar("DELETE FROM detalle_viaje_asiento WHERE idDetalle_Viaje IN (SELECT idDetalle_Viaje FROM detalle_viaje WHERE idViaje = %s)", (id,), auto_commit=False)
            conexion.ejecutar("DELETE FROM detalle_viaje WHERE idViaje = %s", (id,), auto_commit=False)
            conexion.ejecutar("DELETE FROM detalle_personal WHERE idViaje = %s", (id,), auto_commit=False)
            conexion.ejecutar("DELETE FROM viaje WHERE id = %s", (id,), auto_commit=False)

            conexion.conn.commit()
            return {'@MSJ': 'Viaje eliminado correctamente', '@MSJ2': ''}
        except Exception as e:
            conexion.conn.rollback()
            return {'@MSJ': '', '@MSJ2': f'Error al eliminar el viaje: {str(e)}'}
        finally:
            conexion.cerrar()

    #DAR DE BAJA
    @classmethod
    def darBaja(cls, id, solo_consulta=False):
        try:
            conexion = bd.Conexion()

            # Verificar si tiene pasajes vendidos
            tiene_pasajes = conexion.obtener("""
                SELECT 1 FROM pasaje p
                INNER JOIN detalle_viaje_asiento dva ON p.idDetalleViajeAsiento = dva.id
                INNER JOIN detalle_viaje dv ON dva.idDetalle_Viaje = dv.id
                INNER JOIN viaje v ON dv.idViaje = v.id
                WHERE v.id = %s
                LIMIT 1
            """, (id,))

            # Verificar si hay al menos un asiento ya no disponible
            asiento_ocupado = conexion.obtener("""
                SELECT 1 FROM detalle_viaje_asiento dva
                INNER JOIN detalle_viaje dv ON dva.idDetalle_Viaje = dv.id
                INNER JOIN viaje v ON dv.idViaje = v.id
                WHERE dva.esDisponible = 0 AND v.id = %s
                LIMIT 1
            """, (id,))

            # Lógica codificada:
            if tiene_pasajes or asiento_ocupado:
                mensaje = 'Viaje dado de baja correctamente, se tendrá que realizar reembolso a clientes que lo soliciten'
                modal='¿Estas seguro de dar de baja este viaje? Este viaje tiene pasajes vendidos, se habilitara la opción de reembolso para los clientes afectados.'
            else:
                mensaje = 'Viaje dado de baja correctamente'
                modal='¿Estas seguro de dar de baja este viaje?'


            # Si es solo consulta (previsualización), solo devolvemos el mensaje
            if solo_consulta:
                return {'@MSJ': mensaje, '@MSJ2': '','@MODAL': modal}

            # Ejecutar baja real
            conexion.ejecutar("UPDATE viaje SET estado = 0 WHERE id = %s", (id,), auto_commit=False)
            conexion.conn.commit()

            return {'@MSJ': mensaje, '@MSJ2': '', '@MODAL': modal}

        except Exception as e:
            if not solo_consulta:
                conexion.conn.rollback()
            return {'@MSJ': '', '@MSJ2': f'Error al dar de baja al viaje: {str(e)}'}
        finally:
            conexion.cerrar()


    # @classmethod
    # def darBaja(cls, id):
    #     try:
    #         conexion = bd.Conexion()

    #         result_pasaje = conexion.obtener(""" SELECT 1 FROM pasaje p 
    #                         INNER JOIN detalle_viaje_asiento dva ON p.idDetalleViajeAsiento = dva.id
    #                         INNER JOIN detalle_viaje dv ON dva.idDetalle_Viaje = dv.id
    #                         INNER JOIN viaje v ON dv.idViaje = v.id WHERE v.id = %s LIMIT 1""", (id,))
            
    #         result_asiento = conexion.obtener(""" SELECT 1 FROM detalle_viaje_asiento dva
    #                         INNER JOIN detalle_viaje dv ON dva.idDetalle_Viaje = dv.id
    #                         INNER JOIN viaje v ON dv.idViaje = v.id
    #                         WHERE dva.esDisponible = 0 AND v.id = %s LIMIT 1""", (id,))
            
    #         if result_pasaje or result_asiento:
    #             conexion.ejecutar("UPDATE viaje SET estado = 0 WHERE id = %s", (id,), auto_commit=False)
    #             conexion.conn.commit()
    #             return {'@MSJ': 'Viaje dado de baja correctamente, se tendra que realizar reembolso a clientes que lo soliciten', '@MSJ2': ''}
            
    #         conexion.ejecutar("UPDATE viaje SET estado = 0 WHERE id = %s", (id,), auto_commit=False)
    #         conexion.conn.commit()
    #         return {'@MSJ': 'Viaje dado de baja correctamente', '@MSJ2': ''}
    #     except Exception as e:
    #         conexion.conn.rollback()
    #         return {'@MSJ': '', '@MSJ2': f'Error al dar de baja al viaje: {str(e)}'}
    #     finally:
    #         conexion.cerrar()
            
    @classmethod
    def cambiar_estado_viaje(cls, id, idEstadoViaje):
        try:
            conexion = bd.Conexion()

            conexion.ejecutar(""" UPDATE viaje SET idEstadoViaje = %s WHERE id = %s""", (idEstadoViaje, id,), auto_commit=False)

            conexion.conn.commit()
            return {'@MSJ': 'Viaje cambiado de estado correctamente', '@MSJ2': ''}
        except Exception as e:
            conexion.conn.rollback()
            return {'@MSJ': '', '@MSJ2': f'Error al cambiar estado al viaje: {str(e)}'}
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
                WHERE v.estado = 1 AND v.idEstadoViaje = 1
            """                 
            )
            return lista_origenes
        finally:
            conexion.cerrar()

    @classmethod
    def obtenerDestinosMenosActual(cls, origen_id, destino_id):
        conexion = bd.Conexion()
        try:
            query = """
                SELECT DISTINCT
                    CONCAT(s_origen.ciudad, ' - ', s_destino.ciudad) AS ruta
                FROM detalle_viaje dv
                INNER JOIN sucursal s_origen
                    ON s_origen.id = dv.idSucursalOrigen
                INNER JOIN sucursal s_destino
                    ON s_destino.id = dv.idSucursalDestino
                INNER JOIN viaje v
                    ON v.id = dv.idViaje
                WHERE v.estado = 1
                AND v.idEstadoViaje = 1
                AND NOT (
                        dv.idSucursalOrigen = %s
                    AND dv.idSucursalDestino = %s
                );
            """
            return conexion.obtener(query, (origen_id, destino_id))
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
            WHERE s_origen.ciudad = %s AND s_destino.ciudad = %s AND DATE(dv.fechaSalida) = %s AND vi.estado = 1 AND vi.idEstadoViaje = 1;

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
    
    @classmethod
    def obtener_asientos(cls,id_dv):
        try:
            conexion = bd.Conexion()
            listado = conexion.obtener("""
                SELECT 
                    dva.id AS id_asiento,
                    dva.esDisponible AS estado,
                    h.id_tipo AS tipo_herramienta,
                    a.nombre AS nombre,
                    nh.x_dimension,
                    nh.y_dimension,
                    n.nroPiso,
                    h.icono
                FROM nivel_herramienta nh
                JOIN nivel n ON nh.id_nivel = n.id
                JOIN herramienta h ON nh.id_herramienta = h.id
                INNER JOIN asiento a ON nh.id = a.id_nivel_herramienta
                INNER JOIN detalle_viaje_asiento dva ON dva.idAsiento = a.id
                WHERE dva.idDetalle_Viaje = %s

                UNION

                SELECT 
                    NULL AS id_asiento,
                    NULL AS estado,
                    h.id_tipo,
                    NULL AS nombre,
                    nh.x_dimension,
                    nh.y_dimension,
                    n.nroPiso,
                    h.icono
                FROM nivel_herramienta nh
                JOIN nivel n ON nh.id_nivel = n.id
                JOIN herramienta h ON nh.id_herramienta = h.id
                JOIN tipo_vehiculo tv ON tv.id = n.id_tipo_vehiculo
                JOIN vehiculo v ON v.id_tipo_vehiculo = tv.id
                JOIN viaje vi ON vi.idVehiculo = v.id
                JOIN detalle_viaje dv ON dv.idViaje = vi.id
                WHERE dv.id = %s AND h.id_tipo != 1;
                
           """, (id_dv,id_dv))

            return listado
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_tamano_niveles(cls,id):
        conexion = bd.Conexion()
        try:
            niveles = conexion.obtener("""
                SELECT DISTINCT n.id as nivel_id, n.x_dimension as x, n.y_dimension as y
                FROM detalle_viaje dv INNER JOIN viaje v ON dv.idViaje = v.id
                INNER JOIN vehiculo ve ON ve.id = v.idVehiculo
                INNER JOIN tipo_vehiculo tv ON tv.id = ve.id_tipo_vehiculo
                INNER JOIN nivel n ON n.id_tipo_vehiculo = tv.id
                WHERE dv.id = %s
                             """,(id,))
            return niveles
        except:
            conexion.cerrar()

    @classmethod
    def obtener_clientes_por_viaje(cls, id_viaje):
        conexion = None
        try:
            conexion = bd.Conexion()
            return conexion.obtener("""
                 SELECT 
                   cli.email,
                   pas.codigo,
                   asi.nombre as asiento
                FROM pasaje pas
                INNER JOIN venta v 
                    ON pas.idVenta = v.id
                INNER JOIN cliente cli 
                    ON v.idCliente = cli.id
                INNER JOIN detalle_viaje_asiento dvas
                    ON pas.idDetalleViajeAsiento = dvas.id
                INNER JOIN asiento asi 
                	ON asi.id=dvas.idAsiento
                INNER JOIN detalle_viaje dv
                    ON dvas.idDetalle_Viaje = dv.id
                INNER JOIN viaje vi 
                	ON dv.idViaje=vi.id
                WHERE vi.id= %s;
            """,(id_viaje))
        finally:
            if conexion:
                conexion.cerrar()