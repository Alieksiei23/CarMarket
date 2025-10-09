from django.test import TestCase
from unittest.mock import patch, MagicMock
from order.tasks import offer_task


class TestOfferTask(TestCase):

    @patch('order.tasks.Order.objects.create')
    @patch('order.tasks.Showroom.objects.get')
    @patch('order.tasks.Car.objects.filter')
    @patch('order.tasks.Buyer.objects.get')
    def test_offer_success(self, mock_get_buyer, mock_car_filter, mock_get_showroom, mock_order_create):
        mock_buyer = MagicMock()
        mock_buyer.balance = 15000
        mock_get_buyer.return_value = mock_buyer

        mock_car = MagicMock()
        mock_car.model = "sedan"
        mock_car.price = 10000
        mock_car.user.id = 1
        mock_car.is_active = True
        mock_car_filter.return_value.order_by.return_value.first.return_value = mock_car

        mock_showroom = MagicMock()
        mock_get_showroom.return_value = mock_showroom

        result = offer_task(user_id=1, model='model', max_price=11000)

        self.assertEqual(result, {"message": "offer success"})
        mock_car.save.assert_called_once()
        mock_buyer.save.assert_called_once()
        mock_order_create.assert_called_once()
        mock_car.delete.assert_called_once()

    @patch('order.tasks.Buyer.objects.get')
    def test_offer_not_enough_money(self, mock_get_buyer):
        mock_buyer = MagicMock()
        mock_buyer.balance = 15000
        mock_get_buyer.return_value = mock_buyer

        result = offer_task(user_id=1, model='sedan', max_price=25000)

        self.assertEqual(result, {"message": "there are no money"})

    @patch('order.tasks.Buyer.objects.get')
    @patch('order.tasks.Car.objects.filter')
    def test_offer_no_cars(self, mock_car_filter, mock_get_buyer):
        mock_buyer = MagicMock()
        mock_buyer.balance = 15000
        mock_get_buyer.return_value = mock_buyer

        mock_qs = MagicMock()
        mock_qs.order_by.return_value.first.return_value = []
        mock_car_filter.return_value = mock_qs

        result = offer_task(user_id=1, model='sedan', max_price=11000)

        self.assertEqual(result, {"message": "there are no suitable cars available"})