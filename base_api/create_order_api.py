from http_client import HttpClient, HttpMethods
from base_urls import *


class CreateOrderAPI:
    def __init__(self, base_url):
        self.client = HttpClient(base_url)

    def create_order(self, first_name, last_name, address, metro_station, phone, rent_time, delivery_date, comment, color=None):
        endpoint = CREATE_ORDERS_ENDPOINT
        data = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment,
            "color": color
        }
        response = self.client.send_request(HttpMethods.POST, endpoint, json=data)
        return response
