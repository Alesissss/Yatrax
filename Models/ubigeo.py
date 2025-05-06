import bd
import requests
from functools import lru_cache

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
            # Primero intenta búsqueda exacta
            query = """
                SELECT ubigeo FROM ubigeo 
                WHERE UPPER(departamento) = UPPER(%s) 
                AND UPPER(provincia) = UPPER(%s) 
                AND UPPER(distrito) = UPPER(%s)
            """
            resultado = conexion.obtener(query, (departamento, provincia, distrito))
            
            if not resultado:
                # Si no encuentra, intenta búsqueda aproximada
                query = """
                    SELECT ubigeo FROM ubigeo 
                    WHERE UPPER(departamento) LIKE UPPER(%s) 
                    AND UPPER(provincia) LIKE UPPER(%s) 
                    AND UPPER(distrito) LIKE UPPER(%s) 
                    LIMIT 1
                """
                resultado = conexion.obtener(query, (
                    f"%{departamento}%",
                    f"%{provincia}%",
                    f"%{distrito}%"
                ))
            
            return resultado[0] if resultado else None
        finally:
            conexion.cerrar()

    @classmethod
    @lru_cache(maxsize=1000)
    def obtener_por_lat_lon(cls, lat, lon):
        url = f"https://nominatim.openstreetmap.org/reverse?format=geojson&lat={lat}&lon={lon}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                address = data.get("address", {})
                
                departamento = address.get("state", "")
                provincia = address.get("region", "")
                distrito = address.get("village") or address.get("town") or address.get("city", "")
                
                 # Obtener UBIGEO desde la base de datos
                ubigeo = cls.obtener_por_datos(departamento, provincia, distrito)
                
                return {
                    'ubigeo': ubigeo[0] if ubigeo else None,
                    'direccion': data.get("display_name", ""),
                    'datos_ubicacion': {
                        'departamento': departamento,
                        'provincia': provincia,
                        'distrito': distrito
                    }
                }
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud a Nominatim: {e}")
            return None
        except Exception as e:
            print(f"Error procesando datos de geocodificación: {e}")
            return None
    
    @classmethod
    def obtener_direccion(cls, lat, lon):
        url = f"https://nominatim.openstreetmap.org/reverse?format=geojson&lat={lat}&lon={lon}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                return data.get("display_name", "")
        except Exception as e:
            print(f"Error en geocodificación: {e}")
            return None
    