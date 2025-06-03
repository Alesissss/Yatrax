import bd

class Ruta:
    def __init__(self, id=None, nombre=None, sucursalOrigen=None, sucursalDestino=None, estado=None, estadoProceso=None, estadoRegistro=None, fechaRegistro=None, usuario=None):
        self.id = id
        self.nombre = nombre
        self.sucursalOrigen = sucursalOrigen
        self.sucursalDestino = sucursalDestino
        self.estado = estado
        #Auditoría
        self.estadoProceso = estadoProceso
        self.estadoRegistro = estadoRegistro
        self.fechaRegistro = fechaRegistro
        self.usuario = usuario

    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            rutas = conexion.obtener(""" SELECT r.id, r.nombre, r.distancia_estimada, r.tiempo_estimado, r.tipo, r.estado FROM ruta r""")
            return rutas
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, ruta_id):
        conexion = bd.Conexion()
        try:
            ruta = conexion.obtener("SELECT r.id, r.nombre, r.distancia_estimada, r.tiempo_estimado, r.tipo, r.estado FROM ruta r WHERE r.id = %s", (ruta_id,))
            return ruta[0] if ruta else None
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_escalas_por_ruta(cls, ruta_id):
        conexion = bd.Conexion()
        try:
            escalas = conexion.obtener(""" SELECT es.id, es.nro_orden, es.idSucursal, suc.nombre, es.idRuta from escala es INNER JOIN sucursal suc on es.idSucursal = suc.id WHERE idRuta = %s ORDER BY nro_orden""", (ruta_id,))
            return escalas
        finally:
            conexion.cerrar()

    # REGISTRAR
    @classmethod
    def registrar(cls, nombre, distancia, tiempo, estado, tipo, escalas, usuario):
        try:
            conexion = bd.Conexion()

            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_REGISTRAR_RUTA(%s, %s, %s, %s, %s, %s);", (nombre, distancia, tiempo, estado, tipo, usuario), auto_commit=False)

            # Obtener el mensaje de error y el último idRuta generado
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2, LAST_INSERT_ID() AS idRuta;")
            idRuta = resultado[0]['idRuta']  # Obtener el último ID generado por la ruta
            msj2 = resultado[0]['@MSJ2']

            if msj2:  # Si hay un mensaje de error en msj2
                raise Exception('Error al registrar ruta: ' + msj2)

            # Insertar las escalas
            for escala in escalas:
                conexion.ejecutar("INSERT INTO escala (nro_orden, idSucursal, idRuta, distancia_estimada, tiempo_estimado, usuario) VALUES (%s, %s, %s, %s, %s, %s)",
                                (escala['nroOrden'], escala['id'], idRuta, escala['distancia'], escala['tiempo'], usuario), auto_commit=False)

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
    def editar(cls, id, nombre, distancia, tiempo, tipo, estado, escalas, usuario):
        try:
            conexion = bd.Conexion()
            # Llamar al procedimiento almacenado
            conexion.ejecutar("CALL SP_EDITAR_RUTA(%s, %s, %s, %s, %s, %s);", (id, nombre, distancia, tiempo, tipo, estado), auto_commit=False)

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
                conexion.ejecutar("INSERT INTO escala (nro_orden, idSucursal, idRuta, distancia_estimada, tiempo_estimado, usuario) VALUES (%s, %s, %s, %s, %s, %s)",
                                (escala['nroOrden'], escala['id'], id, escala['distancia'], escala['tiempo'], usuario), auto_commit=False)

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
