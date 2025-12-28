import allure
from helpers.api_client import ApiClient

client = ApiClient()


class TestLoginUser:

    @allure.title("Логин под существующим пользователем")
    def test_login_existing_user(self, registered_user):
        user = registered_user["user"]
        response = client.post("/auth/login", {
            "email": user["email"],
            "password": user["password"]
        })

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Логин с неверным логином и паролем")
    def test_login_invalid_credentials(self):
        response = client.post("/auth/login", {
            "email": "wrong@mail.ru",
            "password": "wrong"
        })

        assert response.status_code == 401
        assert response.json()["success"] is False