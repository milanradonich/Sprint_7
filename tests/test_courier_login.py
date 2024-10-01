import allure
import pytest
import requests
import json
from base_urls import *

from base_api.login_courier_api import LoginCourierAPI


class TestCourierLogin:
    BASE_URL = SCOOTER_BASE_URL
    login_api = LoginCourierAPI(BASE_URL)

    @allure.title("Проверка логина курьера")
    @allure.description("Тест проверяет успешный вход курьера в систему.")
    def test_courier_login_success(self):
        login = "bobosik"
        password = "1234"

        with allure.step("Вызов функции логина в систему"):
            result = self.login_api.login_courier(login=login, password=password)
            response_data = result.json()
        with allure.step("Проверка успешного логина в систему"):
            assert result.status_code == 200
            assert "id" in response_data

    @pytest.mark.parametrize("login, password, expected_status", [
        (None, "1234", 400),
        ("bobosik", None, 504),
        (None, None, 504)
    ])
    @allure.title("Проверка логина курьера без параметров")
    @allure.description("Тест проверяет блокировку входа без обязательного параметра")
    def test_check_login_without_req_argument_error(self, login, password, expected_status):
        with allure.step("Вызов функции логина в систему"):
            result = self.login_api.login_courier(login=login, password=password)
        with allure.step("Проверка неуспешного логина в систему"):
            assert result.status_code == expected_status

    @pytest.mark.parametrize("login, password, expected_status, expected_message", [
        ("bob0sik", "1234", 404, "Учетная запись не найдена"),
        ("bobosik", "1234f", 404, "Учетная запись не найдена"),
        ("bobosik1", "1234f", 404, "Учетная запись не найдена")
    ])
    @allure.title("Проверка логина курьера с некорректными данными")
    @allure.description("Тест проверяет блокировку входа с некорректными данными курьера")
    def test_check_incorrect_login_or_password_error(self, login, password, expected_status, expected_message):
        with allure.step("Вызов функции логина в систему"):
            result = self.login_api.login_courier(login=login, password=password)
        with allure.step("Проверка неуспешного логина в систему"):
            assert result.status_code == expected_status
            assert result.json()["message"] == expected_message




