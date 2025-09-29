from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from main.filters import CarFilter
from car.models import Car
from car.serializers import CarSerializer
from main.permissions import IsOwnerOrReadOnly


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    filter_backends = (DjangoFilterBackend,SearchFilter, OrderingFilter)
    filterset_class = CarFilter
    search_fields = ['model']
    ordering_fields = ['price']