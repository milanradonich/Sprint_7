import allure
import pytest

from base_api.get_orders_list_api import GetOrderListApi
from base_urls import *


class TestGetOrdersList:
    BASE_URL = SCOOTER_BASE_URL
    get_orders_list = GetOrderListApi(BASE_URL)

    @allure.title("Проверка получения списка заказов")
    @allure.description("Тест проверяет, что в ответе содержится список из заказов")
    def test_get_orders_list(self):
        with allure.step("Вызов функции получения заказов"):
            result = self.get_orders_list.get_orders()
            response_json = result.json()
        with allure.step("Проверка, что ответ содержит список заказов"):
            assert result.status_code == 200
            assert "orders" in response_json
            assert isinstance(response_json["orders"], list)
