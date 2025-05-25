from bd import Conexion

class TipoHerramienta:

    @classmethod
    def obtener_todos(cls):
        objConexion = Conexion()
        try:
            
            lista_tipos = objConexion.obtener("SELECT id, nombre FROM tipo_herramienta")
            return lista_tipos
        finally:
            objConexion.cerrar()


