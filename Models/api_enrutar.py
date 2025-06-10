# models/api_enrutar.py
import requests
import logging
from typing import Optional, Dict

class ApiEnrutar:
    def __init__(self, api_key: str = None) -> None:
        self.api_key = api_key or "5b3ce3597851110001cf6248ee3267fd49824a40983b5ec79e79356f"
        self.api_url = "https://api.openrouteservice.org/v2/directions/driving-car"

    def obtener_ruta(self, start_lat: float, start_lng: float, end_lat: float, end_lng: float) -> Optional[Dict]:
        headers = {
            'Authorization': self.api_key
        }
        params = {
            'start': f"{start_lng},{start_lat}",
            'end': f"{end_lng},{end_lat}"
        }

        try:
            response = requests.get(self.api_url, headers=headers, params=params, timeout=5)
            if response.status_code == 200:
                data = response.json()
                features = data.get('features', [])
                if not features:
                    logging.warning("Respuesta sin rutas")
                    return None

                geometry = features[0]['geometry']['coordinates']
                summary = features[0]['properties']['summary']
                return {
                    'route': geometry,
                    'distance': summary['distance'],
                    'duration': summary['duration']
                }
            else:
                logging.warning(f"Error en la API de rutas: {response.status_code} - {response.text}")
                return None
        except Exception as e:
            logging.error(f"Error al conectar con la API de rutas: {e}")
            return None
