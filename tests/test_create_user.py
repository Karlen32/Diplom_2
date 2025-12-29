import allure
import pytest
from helpers.api_client import ApiClient
from data.user_data import generate_user

client = ApiClient()


class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self, user_data, cleanup_user):
        response = client.post("/auth/register", user_data)
        body = response.json()

        cleanup_user.append(body["accessToken"])

        assert response.status_code == 200
        assert body["success"] is True

    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_existing_user(self, registered_user):
        payload = registered_user["user"]
        response = client.post("/auth/register", payload)

        assert response.status_code == 403
        assert response.json()["success"] is False

    @allure.title("Создание пользователя без обязательного поля")
    @pytest.mark.parametrize(
        "missing_field",
        ["email", "password", "name"])
    def test_create_user_without_required_field(self, missing_field):
        payload = generate_user()
        payload.pop(missing_field)

        response = client.post("/auth/register", payload)
        body = response.json()

        assert response.status_code == 403
        assert body["success"] is False