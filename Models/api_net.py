# Models/api_net.py
import logging
import requests
from typing import Optional, List

class ApiNetPe:
    # Lista de tokens disponibles
    tokens = [
        'apis-token-16480.FLvVb9s1uQB18C2CWJdGtQgXQyqpqkgp',
        'apis-token-15226.KoJhSj8sr3mnQTWvEi86Xgnxftmah4xO',
        'apis-token-10876.yALxWPL9iXoRctMHIOMkvy5IkVprqb1s',
        'apis-token-11385.NY0mPBbdLdYOVIDVR8zBj1YGTRAQuwfu',
        'apis-token-10991.GVT9dx9z8fHX6mk6aLB28EJJ0HOOjRk7',
        'apis-token-9660.UmHcExv7ZPMtri7UOubK5dro3zqMUrH8',
        'apis-token-7946.-LODBsCL6vKrK7tS4sh0l3fgi6wK6ElW',
        'apis-token-11030.SCSv4kKYWlHpNtJT2xmm5h0Wd4NEHhOw'
    ]
    
    def __init__(self, token: str = None) -> None:
        # Empieza con el token explícito o el primero de la lista
        self._api_token = token or self.tokens[0]
        self._api_url   = "https://api.apis.net.pe"

    def _get(self, path: str, params: dict) -> Optional[dict]:
        url = f"{self._api_url}{path}"
        headers = {
            "Authorization": f"Bearer {self._api_token}",
            "Referer": "python-requests"
        }

        try:
            response = requests.get(url, headers=headers, params=params, timeout=5)
        except requests.RequestException as e:
            return None

        if response.status_code == 200:
            return response.json()
        else:
            return None

    def get_person(self, dni: str) -> Optional[dict]:
        # Intenta con cada token hasta que uno devuelva datos
        for tok in self.tokens:
            self._api_token = tok
            data = self._get("/v2/reniec/dni", {"numero": dni})
            if data:
                return data
        # Si ninguno funcionó, devuelve None
        return None

    def get_company(self, ruc: str) -> Optional[dict]:
        # Intenta con cada token hasta que uno devuelva datos
        for tok in self.tokens:
            self._api_token = tok
            data = self._get("/v2/sunat/ruc", {"numero": ruc})
            if data:
                return data
        return None