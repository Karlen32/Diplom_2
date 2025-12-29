import allure
from helpers.api_client import ApiClient
from data.ingredients_data import get_ingredients_ids

client = ApiClient()


class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_with_auth(self, authorized_headers):
        response = client.post(
            "/orders",
            {"ingredients": get_ingredients_ids()[:2]},
            authorized_headers
        )

        assert response.status_code == 200

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self):
        response = client.post("/orders", {"ingredients": get_ingredients_ids()[:2]})

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self):
        response = client.post("/orders", {"ingredients": []})

        assert response.status_code == 400
        assert response.json()["success"] is False

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_ingredients(self):
        response = client.post("/orders", {"ingredients": ["123"]})

        assert response.status_code == 500