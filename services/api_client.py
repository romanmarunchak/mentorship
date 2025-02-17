# services/api_client.py

import requests
from config import settings

class ObjectResource:
    def __init__(self, base_url):
        self.base_url = f"{base_url}/objects"

    def create(self, data):
        response = requests.post(self.base_url, json=data)
        response.raise_for_status()
        return response.json()

    def get(self, object_id):
        response = requests.get(f"{self.base_url}/{object_id}")
        response.raise_for_status()
        return response.json()

    def update(self, object_id, data):
        response = requests.put(f"{self.base_url}/{object_id}", json=data)
        response.raise_for_status()
        return response.json()

    def delete(self, object_id):
        response = requests.delete(f"{self.base_url}/{object_id}")
        response.raise_for_status()
        return response.status_code


class ApiClient:
    def __init__(self, base_url=settings.BASE_API_URL):
        self.base_url = base_url.rstrip("/")
        self._objects = None

    @property
    def objects(self):
        if self._objects is None:
            self._objects = ObjectResource(self.base_url)
        return self._objects
