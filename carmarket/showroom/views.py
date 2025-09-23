from rest_framework import viewsets

from main.permissions import IsOwnerOrReadOnly
from showroom.models import Showroom, Sale
from showroom.serializers import ShowroomSerializer, SaleSerializer


class ShowroomViewSet(viewsets.ModelViewSet):
    queryset = Showroom.objects.all()
    serializer_class = ShowroomSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = (IsOwnerOrReadOnly,)
