import bd
import requests

class Ubigeo:
    def __init__(self, ubigeo, departamento, provincia, distrito):
        self.ubigeo = ubigeo
        self.departamento = departamento
        self.provincia = provincia
        self.distrito = distrito

    @classmethod
    def obtener_todos(cls):
        conexion = bd.Conexion()
        try:
            query = """
                SELECT ubigeo, departamento, provincia, distrito
                FROM ubigeo
            """
            return conexion.obtener(query)
        finally:
            conexion.cerrar()
    
    @classmethod
    def obtener_por_ubigeo(cls, ubigeo):
        conexion = bd.Conexion()
        try:
            query = """
                SELECT ubigeo, departamento, provincia, distrito
                FROM ubigeo WHERE ubigeo = %s
            """
            resultado = conexion.obtener(query, (ubigeo,))
            return resultado[0] if resultado else None
        finally:
            conexion.cerrar()
    
    @classmethod
    def obtener_por_datos(cls, departamento, provincia, distrito):
        conexion = bd.Conexion()
        try:
            query = """
                SELECT ubigeo
                FROM ubigeo WHERE departamento = %s AND provincia = %s AND distrito = %s
            """
            resultado = conexion.obtener(query, (departamento, provincia, distrito))
            return resultado[0] if resultado else None
        finally:
            conexion.cerrar()

    @classmethod
    def obtener_por_lat_lon(cls, lat, lon):
        url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=jsonv2"
        headers = {'User-Agent': 'Mozilla/5.0'}
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                address = data.get("address", {})
                
                departamento = address.get("state", "")
                provincia = address.get("region", "")
                distrito = address.get("village") or address.get("town") or address.get("city", "")
                
                return cls.obtener_por_datos(departamento, provincia, distrito)
        except Exception as e:
            print(f"Error en geocodificación: {e}")
            return None