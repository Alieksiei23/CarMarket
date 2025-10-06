from rest_framework.test import APIClient, APITestCase

from tests.register_fixtures import Registration


class TestAddCar(Registration):
    car_data = {
        "user": 1,
        "model": "sedan",
        "price": 11000,
        "description": "nice car"
    }
    car_url = '/api/v1/car/'

    def test_add_car_by_showroom(self):
        self.register_and_authenticate(user_type=2)
        response = self.client.post(self.car_url, self.car_data)
        self.assertEqual(response.status_code, 201)

        car = self.client.get(self.car_url).data[0]
        self.assertEqual(car['model'], 'sedan')
        self.assertEqual(car['description'], 'nice car')
        self.assertEqual(car['price'], 11000)

    def test_add_car_by_seller(self):
        self.register_and_authenticate(user_type=3)
        response = self.client.post(self.car_url, self.car_data)
        self.assertEqual(response.status_code, 201)

        car = self.client.get(self.car_url).data[0]
        self.assertEqual(car['model'], 'sedan')
        self.assertEqual(car['description'], 'nice car')
        self.assertEqual(car['price'], 11000)



class TestNegativeCar(APITestCase):
    def setUp(self):
        client = APIClient()
        self.car_data = {
            "model": "sedan",
            "price": 11000,
            "description": "nice car"
        }
        self.car_url = '/api/v1/car/'

    def test_without_price(self):
        del self.car_data['price']
        response = self.client.post(self.car_url, self.car_data)
        self.assertEqual(response.status_code, 400)

    def test_without_model(self):
        del self.car_data['model']
        response = self.client.post(self.car_url, self.car_data)
        self.assertEqual(response.status_code, 400)
