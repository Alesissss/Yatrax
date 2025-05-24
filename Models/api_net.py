from typing import List, Optional
import logging
import requests

# Models/api_net.py
import logging
import requests
from typing import Optional, List

class ApiNetPe:
    def __init__(self, token: str = None) -> None:
        self._api_token = token or 'apis-token-15226.KoJhSj8sr3mnQTWvEi86Xgnxftmah4xO'
        self._api_url = "https://api.apis.net.pe"

    def _get(self, path: str, params: dict):
        url = f"{self._api_url}{path}"
        headers = {
            "Authorization": f"Bearer {self._api_token}",
            "Referer": "python-requests"
        }

        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            logging.warning(f"API Error {response.status_code}: {response.text}")
            return None

    def get_person(self, dni: str) -> Optional[dict]:
        return self._get("/v2/reniec/dni", {"numero": dni})

    def get_company(self, ruc: str) -> Optional[dict]:
        return self._get("/v2/sunat/ruc", {"numero": ruc})

        
        
        
    