from rest_framework import viewsets

from showroom.models import Showroom, Sale
from showroom.serializers import ShowroomSerializer, SaleSerializer


class ShowroomViewSet(viewsets.ModelViewSet):
    queryset = Showroom.objects.all()
    serializer_class = ShowroomSerializer


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
