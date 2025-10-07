from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend

from main.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from order.models import Order, Sale
from order.serializers import OrderSerializer, SaleSerializer
from order.tasks import offer_task
from main.filters import DateFilter

class OrderViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DateFilter


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class OfferView(APIView):

    def post(self, request):
        user_id = int(request.user_id)
        model = request.data['model']
        money = int(request.data['money'])
        offer_task.delay(user_id, model, money)
        return Response({"message": "success"})
