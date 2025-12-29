import requests

BASE_URL = "https://stellarburgers.education-services.ru/api"


class ApiClient:
    def post(self, path, data=None, headers=None):
        return requests.post(f"{BASE_URL}{path}", json=data, headers=headers)

    def get(self, path, headers=None):
        return requests.get(f"{BASE_URL}{path}", headers=headers)

    def patch(self, path, data=None, headers=None):
        return requests.patch(f"{BASE_URL}{path}", json=data, headers=headers)

    def delete(self, path, headers=None):
        return requests.delete(f"{BASE_URL}{path}", headers=headers)