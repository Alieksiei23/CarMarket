from django.test import TestCase
from unittest.mock import patch, MagicMock


from order.tasks import buy_car_by_showroom, offer_by_showroom


class TestBuyCarByShowroom(TestCase):

    @patch('order.tasks.Order.objects.filter')
    def test_buy_car_by_showroom_without_orders(self, mock_get_orders):
        mock_get_orders.return_value = []

        result = buy_car_by_showroom()

        self.assertEqual(
            result,
            {"message": "there have been no orders for the last ten minutes"}
        )

    @patch('order.tasks.offer_by_showroom')
    @patch('order.tasks.Order.objects.filter')
    def test_buy_car_by_showroom_with_orders(self, mock_get_orders, mock_offer_by_showroom):
        obj1 = MagicMock()
        obj2 = MagicMock()
        mock_get_orders.return_value = [obj1, obj2]

        mock_offer_by_showroom.return_value = None

        result = buy_car_by_showroom()

        self.assertEqual(
            result,
            {"message": "orders executed"}
        )



class TestOfferByShowroom(TestCase):

    @patch("order.tasks.Order.objects.create")
    @patch("order.tasks.Seller.objects.get")
    @patch("order.tasks.Car.objects.filter")
    @patch("order.tasks.Sale.objects.filter")
    @patch("order.tasks.Showroom.objects.get")
    def test_offer_by_showroom(self, mock_get_showroom,
                               mock_sale_filter, mock_car_filter,
                               mock_get_seller,mock_order_create,
                               ):

        mock_showroom = MagicMock()
        mock_showroom.id = 1
        mock_showroom.balance = 100_000

        mock_seller = MagicMock()
        mock_seller.user_id = 10
        mock_seller.id = 100
        mock_seller.balance = 100_000
        mock_seller2 = MagicMock()
        mock_seller2.user_id = 11
        mock_seller2.id = 111
        mock_seller2.balance = 100_000
        mock_showroom.seller.all.return_value = [mock_seller, mock_seller2]

        mock_get_showroom.return_value = mock_showroom

        mock_sale = MagicMock()
        mock_sale.seller.id = 10
        mock_sale.discount = 99

        mock_sale_filter.return_value = [mock_sale]


        mock_car = MagicMock()
        mock_car.model = "sedan"
        mock_car.is_active = True
        mock_car.user_id = 10
        mock_car.price = 1_000_000
        mock_car2 = MagicMock()
        mock_car2.model = "sedan"
        mock_car2.is_active = True
        mock_car2.user_id = 11
        mock_car2.price = 100_000

        mock_car_filter.return_value = [mock_car, mock_car2]

        mock_seller = MagicMock()
        mock_seller.balance = 10_000
        mock_get_seller.return_value = mock_seller

        cost_of_car = mock_car.price * (1 - mock_sale.discount / 100)
        money_showroom = mock_showroom.balance - cost_of_car
        money_seller = mock_seller.balance + cost_of_car
        offer_by_showroom(id_showroom=1, model="sedan")


        self.assertEqual(mock_showroom.balance, money_showroom)
        mock_showroom.save.assert_called_once()

        self.assertEqual(mock_seller.balance, money_seller)
        mock_seller.save.assert_called_once()

        mock_car.delete.assert_called_once()

        mock_order_create.assert_called_once_with(
                model="sedan",
                description="buy_car_in_seller",
                price=cost_of_car,
                showroom=mock_showroom,
                seller=mock_seller,
            )
