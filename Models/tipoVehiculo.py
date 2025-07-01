import bd
import hashlib

class TipoVehiculo:
    def __init__(self,idTipoVehiculo=None,nombre=None,idMarca=None,estado=None,cantidad=None):
        self.idTipoVehiculo=idTipoVehiculo
        self.nombre=nombre
        self.idMarca=idMarca
        self.estado=estado
        self.cantidad=cantidad

    @classmethod
    def obtener_todos(cls):
        try:
            conexion = bd.Conexion()
            listado = conexion.obtener("""
                SELECT 
                    tv.id AS id,
                    tv.nombre AS nombre,
                    m.id as id_marca,
                    m.nombre AS marca,
                    s.id as id_servicio,
                    s.nombre AS servicio,
                    tv.estado
                FROM tipo_vehiculo tv
                LEFT JOIN marca m ON tv.id_marca = m.id
                LEFT JOIN servicio s ON tv.id_servicio = s.id 
                GROUP BY 
                    tv.id, 
                    tv.nombre,
                    m.id,
                    m.nombre,
                    s.id,
                    s.nombre,
                    tv.estado;
            """)
            return listado
        finally:
            conexion.cerrar()
    
    @classmethod
    def obtenerUno(cls,idTipoVehiculo):
        try:
            conexion = bd.Conexion()
            listado = conexion.obtener("""
                SELECT 
                    id AS id,
                    nombre,
                    id_marca,
                    id_servicio,
                    estado
                FROM tipo_vehiculo where id=%s
            """,(idTipoVehiculo,))
            return listado[0] if listado else None
        except Exception as e:
            print(f"Error en obtenerUno: {str(e)}")
            raise
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def insertarTipoVehiculo(cls, nombre, idmarca, estado, servicio, usuario, niveles):
        conexion = bd.Conexion()
        try:
            conexion.conn.begin()
            # 1) Insertar el tipo de vehículo
            cursor = conexion.ejecutar(
                "INSERT INTO tipo_vehiculo(nombre, id_marca, id_servicio, estado, usuario) "
                "VALUES (%s, %s, %s, %s, %s)",
                (nombre, idmarca, servicio, estado, usuario),
                auto_commit=False
            )
            id_tipo_vehiculo = cursor.lastrowid

            # 2) Insertar niveles y sus herramientas
            for nivel in niveles:
                cursor = conexion.ejecutar(
                    "INSERT INTO nivel(nroPiso, id_tipo_vehiculo, x_dimension, y_dimension, estado) "
                    "VALUES (%s, %s, %s, %s, %s)",
                    (nivel['nroPiso'], id_tipo_vehiculo, nivel['x_dimension'], nivel['y_dimension'], 1),
                    auto_commit=False
                )
                id_nivel = cursor.lastrowid

                for herramienta in nivel['herramientas']:
                    conexion.ejecutar(
                        "INSERT INTO nivel_herramienta(id_nivel, id_herramienta, x_dimension, y_dimension) "
                        "VALUES (%s, %s, %s, %s)",
                        (id_nivel, herramienta['tipo'], herramienta['x'], herramienta['y']),
                        auto_commit=False
                    )

            conexion.conn.commit()
            print("Éxito al insertar TipoVehículo")
        except Exception as e:
            conexion.conn.rollback()
            print(f"Error en insertarTipoVehiculo: {e}")
            raise
        finally:
            conexion.cerrar()


    @classmethod
    def actualizarTipoVehiculo(cls, id, nombre, marca, estado, servicio, niveles, usuario):
        conexion = bd.Conexion()
        try:
            conexion.conn.begin()

            # 1) Validar que NO haya ningún vehículo de este tipo asignado a un viaje
            existe_en_viaje = conexion.obtener(
                """
                SELECT 1
                  FROM viaje vi
                 INNER JOIN vehiculo v  ON v.id = vi.idVehiculo
                 WHERE v.id_tipo_vehiculo = %s
                 LIMIT 1
                """,
                (id,)
            )
            if existe_en_viaje:
                raise Exception(
                    "No se puede modificar: hay al menos un vehículo de este tipo asignado a un viaje."
                )

            # 2) Actualizar datos del tipo de vehículo
            conexion.ejecutar(
                """
                UPDATE tipo_vehiculo
                   SET nombre      = %s,
                       id_marca    = %s,
                       id_servicio = %s,
                       estado      = %s
                 WHERE id = %s
                """,
                (nombre, marca, servicio, estado, id),
                auto_commit=False
            )

            # 3) Obtener niveles actuales y mapearlos por nroPiso
            niveles_actuales = conexion.obtener(
                "SELECT id, nroPiso FROM nivel WHERE id_tipo_vehiculo = %s",
                (id,)
            )
            mapa_niveles = {n['nroPiso']: n['id'] for n in niveles_actuales}
            pisos_actuales = set(mapa_niveles.keys())
            pisos_nuevos = set(n['nroPiso'] for n in niveles)

            # 4) Eliminar los niveles que ya no vienen
            a_eliminar = pisos_actuales - pisos_nuevos
            if a_eliminar:
                placeholders = ",".join(["%s"] * len(a_eliminar))
                sql = f"DELETE FROM nivel WHERE id_tipo_vehiculo = %s AND nroPiso IN ({placeholders})"
                conexion.ejecutar(sql, (id, *a_eliminar), auto_commit=False)

            # 5) Insertar/Actualizar niveles y sincronizar herramientas
            for nivel in niveles:
                nro = nivel['nroPiso']
                x_dim = nivel['x_dimension']
                y_dim = nivel['y_dimension']
                if nro in mapa_niveles:
                    # Actualizar nivel existente
                    id_nivel = mapa_niveles[nro]
                    conexion.ejecutar(
                        "UPDATE nivel SET x_dimension = %s, y_dimension = %s, estado = 1 WHERE id = %s",
                        (x_dim, y_dim, id_nivel),
                        auto_commit=False
                    )
                else:
                    # Insertar nuevo nivel
                    cursor = conexion.ejecutar(
                        "INSERT INTO nivel(id_tipo_vehiculo, nroPiso, x_dimension, y_dimension, estado) "
                        "VALUES (%s, %s, %s, %s, 1)",
                        (id, nro, x_dim, y_dim),
                        auto_commit=False
                    )
                    id_nivel = cursor.lastrowid

                # Sincronizar herramientas de este nivel
                actuales = conexion.obtener(
                    "SELECT id_herramienta, x_dimension, y_dimension FROM nivel_herramienta WHERE id_nivel = %s",
                    (id_nivel,)
                )
                set_act = {(h['id_herramienta'], h['x_dimension'], h['y_dimension']) for h in actuales}
                set_nue = {(int(h['tipo']), int(h['x']), int(h['y'])) for h in nivel['herramientas']}

                # Insertar las herramientas nuevas
                for h in set_nue - set_act:
                    conexion.ejecutar(
                        "INSERT INTO nivel_herramienta(id_nivel, id_herramienta, x_dimension, y_dimension) "
                        "VALUES (%s, %s, %s, %s)",
                        (id_nivel, h[0], h[1], h[2]),
                        auto_commit=False
                    )
                # Eliminar las herramientas que ya no vienen
                for h in set_act - set_nue:
                    conexion.ejecutar(
                        "DELETE FROM nivel_herramienta "
                        " WHERE id_nivel = %s AND id_herramienta = %s "
                        "   AND x_dimension = %s AND y_dimension = %s",
                        (id_nivel, h[0], h[1], h[2]),
                        auto_commit=False
                    )
            
            vehiculos = conexion.obtener(
                "SELECT id FROM vehiculo WHERE id_tipo_vehiculo = %s",
                (id,)
            )

            for v in vehiculos:
                # Regenerar asientos para cada vehículo de este tipo
                conexion.ejecutar(
                    "DELETE FROM asiento WHERE id_vehiculo = %s",
                    (v['id'],),
                    auto_commit=False
                )
                cursor = conexion.ejecutar(
                    """
                    SELECT nh.id AS id, nh.x_dimension AS x, nh.y_dimension AS y
                      FROM tipo_vehiculo tv
                      INNER JOIN nivel n ON tv.id = n.id_tipo_vehiculo
                      INNER JOIN nivel_herramienta nh ON nh.id_nivel = n.id
                      INNER JOIN herramienta h ON nh.id_herramienta = h.id
                     WHERE h.id_tipo = 1 AND tv.id = %s
                    """,
                    (id,),
                    auto_commit=False
                )
                lista_codigos = cursor.fetchall()
                for codigo in lista_codigos:
                    id_nh = codigo['id']
                    fila = codigo['x']
                    columna = int(codigo['y'])
                    letra = chr(64 + columna)
                    nombre = f"{letra}{fila}"
                    conexion.ejecutar(
                        "INSERT INTO asiento (nombre, id_vehiculo, id_nivel_herramienta, estado, usuario) "
                        "VALUES (%s, %s, %s, 1, %s)",
                        (nombre, v['id'], id_nh, usuario),
                        auto_commit=False
                    )


            conexion.conn.commit()
            return {"MSJ": "Actualización exitosa", "MSJ2": ""}

        except Exception as e:
            conexion.conn.rollback()
            return {"MSJ": "", "MSJ2": f"Error en la actualización: {e}"}
        finally:
            conexion.cerrar()

    @classmethod
    def darBajaTipoVehiculo(cls, idTipoVehiculo):
        conexion = None
        try:
            conexion = bd.Conexion()
            conexion.ejecutar("CALL SP_DARBAJA_TIPOVEHICULO(%s,@MSJ, @MSJ2)", (idTipoVehiculo,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def eliminarTipoVehiculo(cls, idTipoVehiculo):
        conexion = None
        try:
            conexion = bd.Conexion()
            conexion.ejecutar("CALL SP_ELIMINAR_TIPOVEHICULO(%s,@MSJ, @MSJ2)", (idTipoVehiculo,))
            resultado = conexion.obtener("SELECT @MSJ, @MSJ2;")
            return resultado[0]
        finally:
            if conexion:
                conexion.cerrar()
    @classmethod
    def obtener_niveles_por_tipoVehiculo(cls, id_tipo_vehiculo):
        conexion = None
        try:
            conexion = bd.Conexion()

            # Obtener todos los niveles de este tipo de vehículo
            niveles = conexion.obtener(
                "SELECT id, nroPiso, x_dimension, y_dimension, estado FROM nivel WHERE id_tipo_vehiculo = %s ORDER BY nroPiso ASC",
                (id_tipo_vehiculo,)
            )

            # Para cada nivel, obtener sus herramientas
            for nivel in niveles:
                id_nivel = nivel['id']
                herramientas = conexion.obtener(
                    "SELECT id_herramienta, x_dimension, y_dimension FROM nivel_herramienta WHERE id_nivel = %s",
                    (id_nivel,)
                )
                nivel['herramientas'] = herramientas

            return niveles  # lista de dicts, cada uno con su info y sus herramientas

        finally:
            if conexion:
                conexion.cerrar()