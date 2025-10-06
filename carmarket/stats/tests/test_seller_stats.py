from unittest.mock import patch, MagicMock

from django.db.models import QuerySet

from tests.register_fixtures import Registration

class TestSellerStatsView(Registration):

    @patch("stats.views.Seller.objects.get")
    @patch("stats.views.Order.objects.filter")
    def test_seller_stats(self, mock_order, mock_get_seller):
        self.register_and_authenticate(user_type=3)

        mock_seller = MagicMock()
        mock_seller.pk = 1
        mock_get_seller.return_value = mock_seller

        order = MagicMock()
        order.showroom.username = "BMW"
        order.price = 100_000
        order.model = "sedan"

        order2 = MagicMock()
        order2.showroom.username = "AUDI"
        order2.price = 50_000
        order2.model = "sedan"

        order3 = MagicMock()
        order3.showroom.username = "BMW"
        order3.price = 150_000
        order3.model = "jeep"

        mock_order.return_value = [order, order2, order3]
        stats_seller_url = '/api/v1/stats/seller/'
        result = self.client.get(stats_seller_url)
        self.assertEqual(result.status_code, 200)
