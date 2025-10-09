import re
from django.core import mail
from rest_framework.test import APIClient, APITestCase


class Registration(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.registration_url = '/api/v1/auth/users/'
        self.activate_url = '/api/v1/auth/users/activation/'
        self.token_url = '/api/v1/auth/token/'
        self.base_user_data = {
            "email": "test@test.com",
            "username": "test_user",
            "password": "testpass123",
            "re_password": "testpass123",
            "balance": 10000.0,
            "description": "about seller",
            "location": "RU"
        }

    def register_and_authenticate(self, user_type):
        user_data = {**self.base_user_data, "user_type": user_type}
        self.client.post(self.registration_url, user_data)

        letter = mail.outbox[0].body
        match = re.search(r'/auth/verify/(?P<uid>[^/]+)/(?P<token>[^/]+)/', letter)
        uid, token = match['uid'], match['token']
        self.client.post(self.activate_url, {'uid': uid, 'token': token})

        response = self.client.post(self.token_url, {
            "email": user_data['email'],
            "password": user_data['password']
        })
        access_token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + access_token)