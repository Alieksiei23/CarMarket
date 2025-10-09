from unittest.mock import patch, MagicMock


from tests.register_fixtures import Registration

class TestBuyerStatsView(Registration):

    @patch("stats.views.Order.objects.filter")
    def test_buyer_stats_to_one_person(self, mock):
        self.register_and_authenticate(user_type=1)

        mock_order = MagicMock()
        mock_order.model = "sedan"
        mock_order.price = 1000

        mock_order2 = MagicMock()
        mock_order2.model = "jeep"
        mock_order2.price = 10_000

        mock.return_value = [mock_order, mock_order2]

        stats_buyer_url = '/api/v1/stats/buyer/'
        result = self.client.get(stats_buyer_url)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(
            result.data,
            {'spending': 11000, 'models': ['sedan', 'jeep']}
        )

    @patch("stats.views.Order.objects.all")
    def test_buyer_stats_to_many_person(self, mock):

        order = MagicMock()
        order.buyer.username = "Petya"
        order.model = "sedan"
        order.price = 1000

        order2 = MagicMock()
        order2.buyer.username = "Petya"
        order2.model = "jeep"
        order2.price = 22_000


        order3 = MagicMock()
        order3.buyer.username = "Galya"
        order3.model = "jeep"
        order3.price = 31_000

        mock.return_value.select_related.return_value = [order, order2, order3]

        stats_buyer_url = '/api/v1/stats/buyer/'
        result = self.client.get(stats_buyer_url)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(
            result.data,
            {'stats':{
                             'Petya': [('sedan', 1000), ('jeep', 22000)],
                             'Galya': [('jeep', 31000)]},
                             'all_spending': {'Petya': 23000, 'Galya': 31000}
            }
        )
