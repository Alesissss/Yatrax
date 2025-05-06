import bd
import requests
from functools import lru_cache
import unicodedata



class Ubigeo:
    
    def normalizar(texto):
        if texto is None:
            return ''
        texto = unicodedata.normalize('NFD', texto)
        texto = texto.encode('ascii', 'ignore').decode('utf-8')
        return texto.strip().upper()
    
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
    def obtener_por_datos_gradual(cls, departamento, provincia, distrito):
        """
        Obtiene UBIGEO con enfoque gradual:
        1. Intenta con departamento, provincia y distrito
        2. Si no encuentra, intenta con departamento y provincia
        3. Si aún no encuentra, intenta solo con departamento
        """
        if not departamento:
            return None

        # Normalizar nombres
        dep = cls.normalizar(departamento)
        prov = cls.normalizar(provincia) if provincia else None
        dist = cls.normalizar(distrito) if distrito else None

        conexion = bd.Conexion()
        try:
            cursor = conexion.conexion.cursor(dictionary=True)
            
            # 1. Intento con los 3 parámetros (si todos están disponibles)
            if dep and prov and dist:
                query = """
                    SELECT ubigeo FROM ubigeo 
                    WHERE UNACCENT(UPPER(departamento)) = UNACCENT(UPPER(%s))
                    AND UNACCENT(UPPER(provincia)) = UNACCENT(UPPER(%s))
                    AND UNACCENT(UPPER(distrito)) = UNACCENT(UPPER(%s))
                    LIMIT 1
                """
                cursor.execute(query, (dep, prov, dist))
                resultado = cursor.fetchone()
                if resultado:
                    return resultado['ubigeo']

            # 2. Intento con departamento y provincia (si provincia está disponible)
            if dep and prov:
                query = """
                    SELECT ubigeo FROM ubigeo 
                    WHERE UNACCENT(UPPER(departamento)) = UNACCENT(UPPER(%s))
                    AND UNACCENT(UPPER(provincia)) = UNACCENT(UPPER(%s))
                    LIMIT 1
                """
                cursor.execute(query, (dep, prov))
                resultado = cursor.fetchone()
                if resultado:
                    return resultado['ubigeo']

            # 3. Intento solo con departamento
            query = """
                SELECT ubigeo FROM ubigeo 
                WHERE UNACCENT(UPPER(departamento)) = UNACCENT(UPPER(%s))
                LIMIT 1
            """
            cursor.execute(query, (dep,))
            resultado = cursor.fetchone()
            
            return resultado['ubigeo'] if resultado else None

        except Exception as e:
            print(f"Error al buscar UBIGEO gradual: {str(e)}")
            return None
        finally:
            if 'cursor' in locals():
                cursor.close()
            conexion.cerrar()
    
    @classmethod
    @lru_cache(maxsize=1000)
    def obtener_por_datos(cls, departamento, provincia, distrito):
        """Obtiene UBIGEO usando nombres de departamento, provincia y distrito"""
        if not all([departamento, provincia, distrito]):
            return None

        # Normalizar nombres (eliminar tildes, convertir a mayúsculas)
        dep = cls.normalizar(departamento)
        prov = cls.normalizar(provincia)
        dist = cls.normalizar(distrito)

        conexion = bd.Conexion()
        try:
            cursor = conexion.conexion.cursor(dictionary=True)
            
            # Consulta mejorada para coincidencias aproximadas
            query = """
                SELECT ubigeo 
                FROM ubigeo 
                WHERE 
                    (UNACCENT(UPPER(departamento)) LIKE CONCAT('%', UNACCENT(UPPER(%s)), '%') OR
                    (UNACCENT(UPPER(departamento)) = UNACCENT(UPPER(%s))
                AND
                    (UNACCENT(UPPER(provincia)) LIKE CONCAT('%', UNACCENT(UPPER(%s)), '%') OR
                    (UNACCENT(UPPER(provincia)) = UNACCENT(UPPER(%s)))
                AND
                    (UNACCENT(UPPER(distrito)) LIKE CONCAT('%', UNACCENT(UPPER(%s)), '%') OR
                    (UNACCENT(UPPER(distrito)) = UNACCENT(UPPER(%s)))
                LIMIT 1
            """
            cursor.execute(query, (dep, dep, prov, prov, dist, dist))
            resultado = cursor.fetchone()
            
            return resultado['ubigeo'] if resultado else None
            
        except Exception as e:
            print(f"Error al buscar UBIGEO: {str(e)}")
            return None
        finally:
            if 'cursor' in locals():
                cursor.close()
            conexion.cerrar()


    @classmethod
    @lru_cache(maxsize=1000)
    def obtener_por_lat_lon(cls, lat, lon):
        """Obtiene UBIGEO usando coordenadas geográficas (priorizando Perú)"""
        url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}&accept-language=es&countrycodes=pe"
        headers = {'User-Agent': 'Mozilla/5.0'}
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                address = data.get('address', {})
                
                # Mapear campos de Nominatim a nuestros nombres
                departamento = address.get('state', '')
                provincia = address.get('county', '') or address.get('city', '') 
                distrito = address.get('town', '') or address.get('village', '') or address.get('suburb', '')
                
                # Si estamos en Lima Metropolitana
                if not provincia and 'Lima' in departamento:
                    provincia = 'Lima'
                    distrito = address.get('suburb', 'Lima')
                
                # Intentar obtener UBIGEO con los datos
                if departamento and provincia and distrito:
                    return {
                        'ubigeo': cls.obtener_por_datos(departamento, provincia, distrito),
                        'direccion': data.get('display_name', ''),
                        'datos_ubicacion': {
                            'departamento': departamento,
                            'provincia': provincia,
                            'distrito': distrito
                        }
                    }
        except Exception as e:
            print(f"Error en geocodificación inversa: {str(e)}")
        
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
    