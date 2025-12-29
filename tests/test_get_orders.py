import allure
from helpers.api_client import ApiClient

client = ApiClient()


class TestGetOrders:

    @allure.title("Получение заказов авторизованным пользователем")
    def test_get_orders_authorized(self, authorized_headers):
        response = client.get("/orders", authorized_headers)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Получение заказов неавторизованным пользователем")
    def test_get_orders_unauthorized(self):
        response = client.get("/orders")

        assert response.status_code == 401
        assert response.json()["success"] is False