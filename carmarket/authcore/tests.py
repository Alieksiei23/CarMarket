from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient

from tests.register_fixtures import Registration

User = get_user_model()


class TestUserRegistrationWithSignal(Registration):

    def test_buyer_registration_create_buyer_profile(self):
        self.register_and_authenticate(user_type=1)

        url = '/api/v1/user/buyer/'
        response_buyer = self.client.get(url).data[0]
        self.assertEqual(response_buyer['id'], 1)
        self.assertEqual(response_buyer['is_active'], True)
        self.assertEqual(response_buyer['username'], 'test_user')
        self.assertEqual(response_buyer['email'], 'test@test.com')
        self.assertEqual(response_buyer['balance'], 10000.0)

    def test_showroom_registration_create_showroom_profile(self):
        self.register_and_authenticate(user_type=2)

        url = '/api/v1/showroom/'
        response_showroom = self.client.get(url).data[0]
        self.assertEqual(response_showroom['id'], 1)
        self.assertEqual(response_showroom['is_active'], True)
        self.assertEqual(response_showroom['username'], 'test_user')
        self.assertEqual(response_showroom['email'], 'test@test.com')
        self.assertEqual(response_showroom['balance'], 10000.0)
        self.assertEqual(response_showroom['seller'], [])
        self.assertEqual(response_showroom['location'], "RU")

    def test_seller_registration_create_seller_profile(self):
        self.register_and_authenticate(user_type=3)

        url = '/api/v1/user/seller/'
        response_seller = self.client.get(url).data[0]
        self.assertEqual(response_seller['id'], 1)
        self.assertEqual(response_seller['is_active'], True)
        self.assertEqual(response_seller['username'], 'test_user')
        self.assertEqual(response_seller['email'], 'test@test.com')
        self.assertEqual(response_seller['description'], "about seller")
        self.assertEqual(response_seller['balance'], 10000.0)


class TestNegativeRegistration(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.registration_url = '/api/v1/auth/users/'
        self.data = {
            "email": "test@test.ru",
            "username": "test_user",
            "user_type": 1,
            "password": "qwerty",
            "re_password": "qwerty",
        }

    def test_without_usertype(self):
        del self.data['user_type']
        response = self.client.post(self.registration_url, self.data)
        self.assertEqual(response.status_code, 400)

    def test_without_password(self):
        del self.data['password']
        response = self.client.post(self.registration_url, self.data)
        self.assertEqual(response.status_code, 400)

    def test_without_username(self):
        del self.data['username']
        response = self.client.post(self.registration_url, self.data)
        self.assertEqual(response.status_code, 400)
