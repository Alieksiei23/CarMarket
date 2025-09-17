from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from order.models import Order
from order.serializers import OrderSerializer


class OrderViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
