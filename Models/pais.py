import bd

class Pais:
    def __init__(self, id=None, nombre=None, name=None, iso2=None, iso3=None, phone_code=None, continente=None):
        self.id = id
        self.nombre = nombre
        self.name = name
        self.iso2 = iso2
        self.iso3 = iso3
        self.phone_code = phone_code
        self.continente = continente

    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            paises = conexion.obtener("SELECT * FROM pais")
            return paises
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_id(cls, pais_id):
        conexion = bd.Conexion()
        try:
            pais = conexion.obtener("SELECT * FROM pais WHERE id = %s", (pais_id,))
            return pais[0] if pais else None
        finally:
            conexion.cerrar()