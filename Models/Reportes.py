import bd

class Reporte:

    @classmethod
    def cantidadUsuariosxTipo(cls):
        # tipo , cantidad
        conexion = None
        try:
            conexion = bd.Conexion()
            resultados = conexion.obtener("select tipUsu.nombre as tipo, count(usu.id) as cantidad from usuarios usu left join tipo_usuario tipUsu on usu.id_tipousuario=tipUsu.id group by tipUsu.nombre;")
            return resultados
        except Exception as e:
            print("Error al obtener la cantidad de usuarios por tipo: ", e)

    @classmethod
    def cantidadUsuariosActivos(cls):
        conexion = None
        try:
            # estado, cantidad
            conexion = bd.Conexion()
            resultados = conexion.obtener("""
                SELECT 
                CASE 
                    WHEN estado = 1 THEN 'Activo'
                    ELSE 'Inactivo'
                END AS estado,
                COALESCE(COUNT(usuarios.id),0) AS cantidad
                FROM usuarios
                GROUP BY usuarios.estado
                ORDER BY COALESCE(COUNT(usuarios.id),0) DESC;
            """)
            return resultados
        except Exception as e:
            print("Error al obtener la cantidad de usuarios activos: ", e)

    @classmethod
    def cantidadPersonalxTipo(cls):
        # tipo, cantidad
        conexion = None
        try:
            conexion = bd.Conexion()
            resultados = conexion.obtener("""
                SELECT tipPer.nombre,COALESCE(COUNT(per.id),0) as cantidad from personal per LEFT JOIN tipo_personal tipPer ON per.id_tipopersonal=tipPer.id GROUP BY tipPer.nombre order by COALESCE(count(per.id),0) DESC;
            """)
            return resultados
        except Exception as e:
            print("Error al obtener la cantidad de personal por tipo: ", e)

    @classmethod
    def cantidadPersonalActivo(cls):
        conexion = None
        try:
            # estado, cantidad
            conexion = bd.Conexion()
            resultados = conexion.obtener("""
                SELECT 
                CASE WHEN per.estado = 1 THEN 'Activo' ELSE 'Inactivo' END AS estado,
                COUNT(per.id) AS cantidad
                FROM personal per
                GROUP BY per.estado
                ORDER BY COUNT(per.id) DESC;
            """)
            return resultados
        except Exception as e:
            print("Error al obtener la cantidad de personal activo: ", e)

    #Falta probar
    @classmethod
    def topRutasSolicitadas(cls):
        # ruta, cantidad
        conexion = None
        try:
            conexion = bd.Conexion()
            resultados = conexion.obtener("""
                SELECT r.nombre AS ruta, COUNT(p.id) AS total_compras
                FROM pasaje p
                INNER JOIN detalle_viaje_asiento dva ON p.idDetalleViajeAsiento = dva.id
                INNER JOIN detalle_viaje dv ON dva.idDetalle_Viaje = dv.id
                INNER JOIN viaje v ON dv.idViaje = v.id
                INNER JOIN ruta r ON v.idRuta = r.id
                GROUP BY r.id, r.nombre
                ORDER BY total_compras DESC
                LIMIT 3;
            """)
            return resultados
        except Exception as e:
            print("Error al obtener la cantidad de rutas solicitadas: ", e)

    @classmethod
    def cantidadRutasProgramadasxMes(cls):
        conexion = None
        try:
            # mes, total_programaciones
            conexion = bd.Conexion()
            resultados = conexion.obtener("""
                SELECT DATE_FORMAT(fechaHoraSalida, '%Y-%m') AS mes, COUNT(*) AS total_programaciones
                FROM viaje
                GROUP BY mes
                ORDER BY mes;
            """)
            return resultados
        except Exception as e:
            print("Error al obtener la cantidad de rutas programadas por mes: ", e)

    @classmethod
    def cantidadIngresosxServicio(cls):
        # servicio, cantidad
        conexion = None
        try:
            conexion = bd.Conexion()
            resultados = conexion.obtener("""
                SELECT 
                    s.nombre AS servicio,
                    COALESCE(COUNT(p.id), 0) AS cantidad_ventas
                FROM servicio s
                LEFT JOIN tipo_vehiculo tv ON s.id = tv.id_servicio
                LEFT JOIN vehiculo ve ON tv.id = ve.id_tipo_vehiculo
                LEFT JOIN viaje vi ON ve.id = vi.idVehiculo
                LEFT JOIN detalle_viaje dv ON vi.id = dv.idViaje
                LEFT JOIN detalle_viaje_asiento dva ON dv.id = dva.idDetalle_Viaje
                LEFT JOIN pasaje p ON dva.id = p.idDetalleViajeAsiento
                GROUP BY s.id, s.nombre
                ORDER BY cantidad_ventas DESC;
            """)
            return resultados[0]
        except Exception as e:
            print("Error al obtener la cantidad de ventas por servicio: ", e)

    #aun falta
    @classmethod
    def cantidadIngresosxPeriodo(cls):
        pass

    @classmethod
    def cantidadClientesxPais(cls):
        conexion = None
        try:
            # pais, cantidad
            conexion = bd.Conexion()
            resultados = conexion.obtener("""
                SELECT 
                    p.nombre AS pais,
                    COALESCE(COUNT(c.id), 0) AS cantidad
                FROM pais p
                LEFT JOIN cliente c ON p.id = c.id_pais
                GROUP BY p.id, p.nombre
                ORDER BY cantidad DESC;
            """)

            return resultados[0]
        except Exception as e:
            print("Error al obtener la cantidad de clientes por pais: ", e)


    @classmethod
    def cantidadClientesxTipo(cls):
        conexion = None
        try:
            # tipo_cliente, cantidad
            conexion = bd.Conexion()
            resultados = conexion.obtener("""
                SELECT 
                    tc.nombre AS tipo_cliente,
                    COALESCE(COUNT(c.id), 0) AS cantidad
                FROM tipo_cliente tc
                LEFT JOIN cliente c ON tc.idTipoCliente = c.id_tipo_cliente
                GROUP BY tc.idTipoCliente, tc.nombre
                ORDER BY cantidad DESC;
            """)
            return resultados[0]
        except Exception as e:
            print("Error al obtener la cantidad de clientes por tipo: ", e)
    



        