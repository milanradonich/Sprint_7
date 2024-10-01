import allure
import pytest
import requests
import json

from base_urls import *
from base_api.create_order_api import CreateOrderAPI


class TestCreateOrder:
    BASE_URL = SCOOTER_BASE_URL
    create_order_api = CreateOrderAPI(BASE_URL)

    @pytest.mark.parametrize("color", [
        (["BLACK", "GREY"]),
        (["BLACK"]),
        (["GREY"]),
        ([])
    ])
    @allure.title("Проверка оформления заказа")
    @allure.description("Тест проверяет успешное оформление заказа с разными параметрами цвета.")
    def test_create_order_success(self, color):
        first_name = "Maxim"
        last_name = "Gorky"
        address = "Polevaya st."
        metro_station = "centr"
        phone = "+7 800 355 35 35"
        rent_time = 1
        delivery_date = "2024-10-10"
        comment = "Saske, come back to Konoha"
        with allure.step("Вызов функции оформления заказа"):
            result = self.create_order_api.create_order(first_name=first_name, last_name=last_name, address=address,
                                                        metro_station=metro_station, phone=phone, rent_time=rent_time,
                                                        delivery_date=delivery_date, comment=comment, color=color)
        with allure.step("Проверка успешного оформления заказа"):
            assert result.status_code == 201
            assert "track" in result.json()
