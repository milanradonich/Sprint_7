from http_client import HttpClient, HttpMethods
from base_urls import *


class GetOrderListApi:
    def __init__(self, base_url):
        self.client = HttpClient(base_url)

    def get_orders(self):
        endpoint = CREATE_ORDERS_ENDPOINT
        response = self.client.send_request(HttpMethods.GET, endpoint, json=None)
        return response

