from rest_framework import viewsets

from car.models import Car
from car.serializers import CarSerializer
from main.permissions import IsOwnerOrReadOnly


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsOwnerOrReadOnly,)
