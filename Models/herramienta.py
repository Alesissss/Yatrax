from bd import Conexion
class Herramienta:

    @classmethod
    def obtener_todos(cls):
        objConexion = Conexion()
        try:
            lista_herramientas = objConexion.obtener("SELECT id, nombre, icono, id_tipo FROM herramienta")
            return lista_herramientas
        finally:
            objConexion.cerrar()

    