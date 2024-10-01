import pytest
import allure
import requests
import json

from base_api.create_courier_api import CourierAPI
from helper import register_new_courier_and_return_login_password
from base_urls import *


class TestRegistration:
    BASE_URL = SCOOTER_BASE_URL
    courier_api = CourierAPI(BASE_URL)

    @allure.title("Проверка регистрации нового курьера")
    @allure.description("Тест проверяет успешную регистрацию нового курьера.")
    def test_registration_new_account_success(self):
        with allure.step("Вызов функции создания нового курьера"):
            status_code, response_data, login_pass = register_new_courier_and_return_login_password()
        with allure.step("Проверка успешного создания курьера"):
            assert status_code == 201
            assert response_data["ok"] == True

    @allure.title("Проверка создания двух одинаковых курьеров")
    @allure.description("Тест проверяет, что нельзя содать двух одинаковых курьеров.")
    def test_cant_create_two_identical_couriers_error(self):
        with allure.step("Вызов функции создания нового курьера"):
            status_code, response_data, login_pass = register_new_courier_and_return_login_password()
        with allure.step("Проверка успешного создания курьера"):
            assert status_code == 201, f"Ожидался ответ 201, но получили {status_code}. Ответ: {response_data}"
        login, password, first_name = login_pass
        with allure.step("Повторный вызов функции создания курьера"):
            response = self.courier_api.create_courier(login, password, first_name)
            result = response.status_code
            result_answer = response.json()
        with allure.step("Проверка, что получаем ошибку при повторном создании курьера"):
            assert result == 409, f"Ожидался ответ 409, но получили {result}. Ответ: {result_answer}"
            assert result_answer["message"] == 'Этот логин уже используется. Попробуйте другой.'

    @pytest.mark.parametrize("login, password", [
        ("barbosik", None),
        (None, "test_password")
    ])
    @allure.title("Проверка регистрации без обязательных аргументов")
    @allure.description("Тест проверяет запрос регистрации без одного обязательного аргумента.")
    def test_check_registration_new_account_without_req_argument_error(self, login, password):
        with allure.step("Вызов функции создания нового курьера"):
            response = self.courier_api.create_courier(login=login, password=password)
        with allure.step("Получение результата после отправки запроса"):
            result = response.status_code
        with allure.step("Проверка получения ошибки без одного аргумента"):
            assert result == 400
            assert response.json()["message"] == 'Недостаточно данных для создания учетной записи'

