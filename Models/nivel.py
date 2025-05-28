import bd
import hashlib

class Nivel:
    def __init__(self, idNivel=None, nroPiso=None, vehiculo=None, cantidad=None, estado=None):
        self.idNivel = idNivel
        self.nroPiso = nroPiso
        self.vehiculo = vehiculo
        self.cantidad = cantidad
        self.estado = estado

    @classmethod
    def obtener_todos(cls):
        conexion = None
        try:
            conexion = bd.Conexion()
            listado = conexion.obtener("""
                SELECT 
                n.id AS id,
                n.nroPiso AS nroPiso,
                v.nombre AS nombre,
                n.estado
            FROM 
                nivel n
            INNER JOIN 
                tipo_vehiculo v ON n.id_tipo_vehiculo = v.id;
            """)
            return listado
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def obtener_uno_por_idNivel(cls, idNivel):
        conexion = None
        try:
            conexion = bd.Conexion()
            cursor = conexion.ejecutar("SELECT id,nroPiso,id_tipo_vehiculo,x_dimension,y_dimension,estado FROM nivel WHERE id=%s",(idNivel,))
            datos_nivel = cursor.fetchone()
            datos_botones = conexion.obtener("select id_herramienta,id_nivel,x_dimension,y_dimension from nivel_herramienta where id_nivel = %s",(idNivel,))
            return datos_nivel, datos_botones
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def obtener_por_tipo_vehiculo(cls, vehiculo):
        conexion = None
        try:
            conexion = bd.Conexion()
            listado = conexion.obtener(
                "SELECT * FROM nivel WHERE id_tipo_vehiculo = %s ORDER BY nroPiso",
                (vehiculo,)
            )
            return listado
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def insertar_nivel(cls, nroPiso, id_tipo_vehiculo,x_dimension,y_dimension,estado,lista_herramientas):
        conexion = bd.Conexion()
        try:
            conexion.conn.begin()
            cursor = conexion.ejecutar("INSERT INTO nivel (nroPiso,id_tipo_vehiculo, x_dimension, y_dimension, estado) VALUES (%s,%s,%s,%s,%s)",(nroPiso, id_tipo_vehiculo,x_dimension,y_dimension,estado),auto_commit=False)
            ultimo_id = cursor.lastrowid
            print(lista_herramientas)
            for herramienta in lista_herramientas:   
                print(herramienta) 
                conexion.ejecutar("INSERT INTO nivel_herramienta (id_herramienta,id_nivel,x_dimension,y_dimension) VALUES (%s,%s,%s,%s)",(herramienta['tipo'],ultimo_id,herramienta['x'],herramienta['y']),auto_commit=False)
            conexion.conn.commit()
            print("Exito")
        except Exception as e:
            print(f"Error: {e}")
            conexion.conn.rollback()
        finally:
            conexion.cerrar()

    @classmethod
    def actualizar_nivel(cls, idNivel, nroPiso, tipo_vehiculo, x_dimension, y_dimension, estado, lista_herramientas):
        conexion = bd.Conexion()
        try:
            conexion.conn.begin()

            conexion.ejecutar(
            """
            UPDATE nivel
            SET nroPiso = %s,
                id_tipo_vehiculo = %s,
                x_dimension = %s,
                y_dimension = %s,
                estado = %s
            WHERE id = %s
            """,
            (nroPiso, tipo_vehiculo, x_dimension, y_dimension, estado, idNivel),
            auto_commit=False
        )

            conexion.ejecutar(
                "DELETE FROM nivel_herramienta WHERE id_nivel = %s",
                (idNivel,),
                auto_commit=False
            )

            for herramienta in lista_herramientas:
                conexion.ejecutar(
                    "INSERT INTO nivel_herramienta (id_herramienta, id_nivel, x_dimension, y_dimension) VALUES (%s, %s, %s, %s)",
                    (herramienta['tipo'], idNivel, herramienta['x'], herramienta['y']),
                    auto_commit=False
                )

            conexion.conn.commit()
            print("Nivel actualizado correctamente.")

        except Exception as e:
            print(f"Error en actualizar_nivel: {e}")
            conexion.conn.rollback()
            raise
        finally:
            if conexion:
                conexion.cerrar()
    @classmethod
    def dar_baja_piso(cls, idNivel):
        conexion = None
        try:
            conexion = bd.Conexion()
            conexion.ejecutar(
                "CALL SP_DARBAJA_PISO(%s)",
                (idNivel,)
            )
            resultado = conexion.obtener("SELECT @MSJ AS MSJ, @MSJ2 AS MSJ2;")
            return resultado[0]["MSJ"], resultado[0]["MSJ2"]
        except Exception as e:
            print(f"Error en dar_baja_piso: {e}")
            raise
        finally:
            if conexion:
                conexion.cerrar()

    @classmethod
    def eliminar_nivel(cls, idNivel):
        conexion = bd.Conexion()
        try:
            conexion.conn.begin()
            conexion.ejecutar("DELETE FROM nivel_herramienta where id_nivel = %s",(idNivel,),auto_commit=False)
            conexion.ejecutar(
                "CALL SP_ELIMINAR_NIVEL(%s)",
                (idNivel,),
                auto_commit=False
            )
            resultado = conexion.obtener("SELECT @MSJ as MSJ, @MSJ2 as MSJ2;")
            conexion.conn.commit()
            return resultado[0]["MSJ"], resultado[0]["MSJ2"]
        except Exception as e:
            conexion.conn.rollback()
            print(f"Error: {e}")
        finally:
            conexion.cerrar()