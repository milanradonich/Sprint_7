from http_client import HttpClient, HttpMethods
from base_urls import *


class LoginCourierAPI:
    def __init__(self, base_url):
        self.client = HttpClient(base_url)

    def login_courier(self, login=None, password=None):
        endpoint = COURIER_LOGIN_ENDPOINT
        data = {
            "login": login,
            "password": password,
        }
        response = self.client.send_request(HttpMethods.POST, endpoint, json=data)
        return response
