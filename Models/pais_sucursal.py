import bd

class PaisSucursal:
    def __init__(self, id=None, pais_id=None, abreviatura=None):
        self.id = id
        self.pais_id = pais_id
        self.abreviatura = abreviatura

    @classmethod
    def obtener_pais_permitido(cls):
        conexion = bd.Conexion()
        try:
            paises_sucursal = conexion.obtener("SELECT * FROM pais_sucursal ps inner join ")
            return paises_sucursal
        finally:
            conexion.cerrar()