import pytest
from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient


User = get_user_model()


class TestUserRegistrationSignal(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.registration_url = '/api/v1/auth/users/'

    def test_buyer_registration_create_buyer_profile(self):
        data = {
            "email": "buyer@test.com",
            "username": "buyer_user",
            "password": "testpass123",
            "re_password": "testpass123",
            "user_type": 1,
            "balance": 1000.0
        }

        response = self.client.post(self.registration_url, data)

        self.assertEqual(response.status_code, 201)


        url = '/api/v1/buyer/'
        response_buyer = self.client.get(url).data[0]
        self.assertEqual(response_buyer['id'], 1)
        self.assertEqual(response_buyer['is_active'], True)
        self.assertEqual(response_buyer['username'], 'buyer_user')
        self.assertEqual(response_buyer['email'], 'buyer@test.com')
        self.assertEqual(response_buyer['balance'], 1000.0)
        self.assertEqual(response_buyer['user'], 1)

    def test_showroom_registration_create_showroom_profile(self):
        data = {
            "email": "showroom@test.com",
            "username": "showroom_user",
            "password": "testpass123",
            "re_password": "testpass123",
            "user_type": 2,
            "location": "RU",
            "balance": 1000.0
        }

        response = self.client.post(self.registration_url, data)
        self.assertEqual(response.status_code, 201)

        url = '/api/v1/showroom/'
        response_showroom = self.client.get(url).data[0]
        self.assertEqual(response_showroom['id'], 1)
        self.assertEqual(response_showroom['is_active'], True)
        self.assertEqual(response_showroom['username'], 'showroom_user')
        self.assertEqual(response_showroom['email'], 'showroom@test.com')
        self.assertEqual(response_showroom['balance'], 1000.0)
        self.assertEqual(response_showroom['user'], 1)
        self.assertEqual(response_showroom['seller'], [])
        self.assertEqual(response_showroom['location'], "RU")


    def test_seller_registration_create_seller_profile(self):
        data = {
            "email": "seller@test.com",
            "username": "seller_user",
            "password": "testpass123",
            "re_password": "testpass123",
            "description": "about seller",
            "user_type": 3,
            "balance": 1000.0
        }

        response = self.client.post(self.registration_url, data)
        self.assertEqual(response.status_code, 201)

        url = '/api/v1/seller/'
        response_seller = self.client.get(url).data[0]
        self.assertEqual(response_seller['id'], 1)
        self.assertEqual(response_seller['is_active'], True)
        self.assertEqual(response_seller['username'], 'seller_user')
        self.assertEqual(response_seller['email'], 'seller@test.com')
        self.assertEqual(response_seller['description'], "about seller")
        self.assertEqual(response_seller['balance'], 1000.0)
        self.assertEqual(response_seller['user'], 1)
