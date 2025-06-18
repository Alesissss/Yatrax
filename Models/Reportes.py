import bd

class Reprote:
    def __init__(self):
        self

    @classmethod
    def cantidadUsuariosxTipo():
        # tipo , cantidad
        conexion = None
        try:
            conexion = bd.Conexion()
            resultados = conexion.obtener("select tipUsu.nombre as tipo, count(usu.id) as cantidad from usuarios usu left join tipo_usuario tipUsu on usu.id_tipousuario=tipUsu.id group by tipUsu.nombre;")
            return resultados[0]
        except Exception as e:
            print("Error al obtener la cantidad de usuarios por tipo: ", e)

    @classmethod
    def cantidadUsuariosActivos():
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
            return resultados[0]
        except Exception as e:
            print("Error al obtener la cantidad de usuarios activos: ", e)

    @classmethod
    def cantidadPersonalxTipo():
        # tipo, cantidad
        conexion = None
        try:
            conexion = bd.Conexion()
            resultados = conexion.obtener("""
                SELECT tipPer.nombre,COALESCE(COUNT(per.id),0) from personal per LEFT JOIN tipo_personal tipPer ON per.id_tipopersonal=tipPer.id GROUP BY tipPer.nombre order by COALESCE(count(per.id),0) DESC;
            """)
            return resultados[0]
        except Exception as e:
            print("Error al obtener la cantidad de personal por tipo: ", e)

    @classmethod
    def cantidadPersonalActivo():
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
            return resultados[0]
        except Exception as e:
            print("Error al obtener la cantidad de personal activo: ", e)

    #Falta probar
    @classmethod
    def topRutasSolicitadas():
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
            return resultados[0]
        except Exception as e:
            print("Error al obtener la cantidad de rutas solicitadas: ", e)




        