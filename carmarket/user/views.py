from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user.models import Buyer, Seller
from user.serializers import BuyerSerializers, SellerSerializer


class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializers
    permission_classes = (IsAuthenticated,)


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
