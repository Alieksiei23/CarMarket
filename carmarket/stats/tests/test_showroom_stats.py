from unittest.mock import patch, MagicMock

from showroom.models import Showroom


from tests.register_fixtures import Registration
from stats.serializers import ShowroomReportSerializer

class ShowroomReportViewTest(Registration):

    @patch("stats.serializers.ShowroomReportSerializer.get_sellers")
    @patch("stats.serializers.ShowroomReportSerializer.get_buyers_amount")
    @patch("stats.serializers.ShowroomReportSerializer.get_orders")
    @patch("stats.serializers.ShowroomReportSerializer.get_profit")
    def test_showroom_stats(self, mock_profit, mock_order, mock_buyers, mock_sellers):
        self.register_and_authenticate(user_type=2)

        mock_profit.return_value = 100_000
        mock_order.return_value = 3
        mock_buyers.return_value = 2
        mock_sellers.return_value = 5

        url = "/api/v1/stats/showroom/"

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = self.client.get(url).data[0]
        self.assertEqual(data['username'], 'test_user')
        self.assertEqual(data['email'], 'test@test.com')
        self.assertEqual(data['orders'], 3)
        self.assertEqual(data['buyers_amount'], 2)
        self.assertEqual(data['sellers'], 5)
