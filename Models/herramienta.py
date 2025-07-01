from bd import Conexion
class Herramienta:

    @classmethod
    def obtener_todos(cls):
        objConexion = Conexion()
        try:
            lista_herramientas = objConexion.obtener("SELECT id, nombre, estado, icono, id_tipo FROM herramienta")
            return lista_herramientas
        finally:
            objConexion.cerrar()

    