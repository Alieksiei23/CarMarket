from django.test import TestCase
from unittest.mock import patch, MagicMock

from order.models import Sale
from order.tasks import chose_best_seller


class TestChoseBestSellerTask(TestCase):

    @patch('order.tasks.Sale.objects.get')
    @patch('order.tasks.Showroom.objects.all')
    def test_chose_best_seller_no_discount(self, mock_get_showroom, mock_get_sale):
        mock_seller1 = MagicMock()
        mock_seller1.username = "first_seller"
        mock_seller2 = MagicMock()
        mock_seller2.username = "second_seller"

        mock_showroom = MagicMock()
        mock_showroom.username = "first_showroom"
        mock_showroom.seller.all.return_value = [mock_seller1, mock_seller2]

        mock_get_showroom.return_value = [mock_showroom]

        mock_get_sale.side_effect = Sale.DoesNotExist

        result = chose_best_seller()

        self.assertEqual(
            result,
            {"message": [("first_showroom", "No discount", 0)]}
        )

    @patch('order.tasks.Sale.objects.get')
    @patch('order.tasks.Showroom.objects.all')
    def test_chose_best_seller_with_discount(self, mock_get_showroom, mock_get_sale):
        mock_seller1 = MagicMock()
        mock_seller1.username = "first_seller"
        mock_seller2 = MagicMock()
        mock_seller2.username = "second_seller"

        mock_showroom = MagicMock()
        mock_showroom.username = "first_showroom"
        mock_showroom.seller.all.return_value = [mock_seller1, mock_seller2]
        mock_showroom2 = MagicMock()
        mock_showroom2.username = "second_showroom"
        mock_showroom2.seller.all.return_value = [mock_seller1, mock_seller2]

        mock_get_showroom.return_value = [mock_showroom, mock_showroom2]

        def sale_side_effect(**kwargs):
            if kwargs['seller'].username == 'second_seller' and kwargs['showroom'].username == 'first_showroom':
                mock_sale = MagicMock()
                mock_sale.discount = 10
                return mock_sale
            elif kwargs['seller'].username == 'first_seller' and kwargs['showroom'].username == 'second_showroom':
                mock_sale = MagicMock()
                mock_sale.discount = 99
                return mock_sale
            else:
                raise Sale.DoesNotExist

        mock_get_sale.side_effect = sale_side_effect

        result = chose_best_seller()

        self.assertEqual(
            result,
            {
                "message": [
                    ('first_showroom', 'second_seller', 10),
                    ('second_showroom', 'first_seller', 99)
                ]
            }
        )
