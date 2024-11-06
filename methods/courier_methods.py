from data import BASE_URL, COURIERS_URL
import json
import requests
import random


class CourierMethods:

    @staticmethod
    def get_random_number():
        return str(random.randint(10000, 99999))

    def __init__(self):
        self.courier_data = {
            "login": 'login_' + self.get_random_number(),
            "password": 'password_' + self.get_random_number(),
            "first_name": 'firstname_' + self.get_random_number()
        }
        self.courier_id = ''

    def post_create_courier(self):
        headers = {"Content-type": "application/json"}
        response = requests.post(f'{BASE_URL}{COURIERS_URL}', data=json.dumps(self.courier_data), headers=headers)
        return response

    def post_login_courier(self):
        data = {
            "login": self.courier_data["login"],
            "password": self.courier_data["password"]
        }

        headers = {"Content-type": "application/json"}
        response = requests.post(f'{BASE_URL}{COURIERS_URL}login', data=json.dumps(data), headers=headers)
        return response

    def delete_courier(self):
        response = requests.delete(f'{BASE_URL}{COURIERS_URL}/{self.courier_id}')
        return response

