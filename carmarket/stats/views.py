from rest_framework.response import Response
from rest_framework.views import APIView
from collections import Counter

from order.models import Order
from showroom.models import Showroom
from stats.serializers import ShowroomReportSerializer

from user.models import Buyer, Seller


class ShowroomReportView(APIView):

    def get(self, request, *args, **kwargs):
        showrooms = Showroom.objects.all()
        serializer = ShowroomReportSerializer(showrooms, many=True)
        return Response(serializer.data)


class BuyerStatsView(APIView):

    def get(self, request):

        try:
            user_id = request.user_id
            orders = Order.objects.filter(
                buyer=Buyer.objects.get(user_id=user_id).pk
            )
            models = []
            spending = 0
            for order in orders:
                models.append(order.model)
                spending += order.price
            return Response({"spending": spending, "models": models})

        except AttributeError:

            orders = Order.objects.all().select_related('buyer')
            result = {}
            result_spending = {}

            for order in orders:
                if order.buyer:
                    result[order.buyer.username] = result.setdefault(order.buyer.username, []) + [(order.model, order.price)]

            for buyer in result:
                spending = sum(i[1] for i in result[buyer])
                result_spending[buyer] = spending

            return Response({'stats': result, 'all_spending': result_spending})


class SellerStatsView(APIView):

    def get(self, request):
        user_id = request.user_id
        orders = Order.objects.filter(
            seller=Seller.objects.get(user_id=user_id).pk
        )
        showrooms = []
        models = []
        profit = 0
        for order in orders:
            showrooms.append(order.showroom.username)
            profit += order.price
            models.append(order.model)

        counter = Counter(showrooms)

        return Response({"profit": profit,
                         "models": models,
                         "buyers": showrooms,
                         "active_buyer": counter.most_common(5)})