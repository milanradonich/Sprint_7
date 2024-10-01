import json
from base_urls import *
from http_client import HttpClient, HttpMethods


class CourierAPI:
    def __init__(self, base_url):
        self.client = HttpClient(base_url)

    def create_courier(self, login=None, password=None, first_name=None):
        endpoint = CREATE_COURIER_ENDPOINT
        data = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        response = self.client.send_request(HttpMethods.POST, endpoint, json=data)
        return response

