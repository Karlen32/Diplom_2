import allure
from helpers.api_client import ApiClient

client = ApiClient()


class TestUpdateUser:

    @allure.title("Изменение данных пользователя с авторизацией")
    def test_update_user_with_auth(self, authorized_user):
        response = client.patch("/auth/user", {"name": "New Name"}, authorized_user)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Изменение данных пользователя без авторизации")
    def test_update_user_without_auth(self):
        response = client.patch("/auth/user", {"name": "Fail"})

        assert response.status_code == 401
        assert response.json()["success"] is False