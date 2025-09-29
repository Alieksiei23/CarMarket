from django_filters import RangeFilter, DateFilter, DateFromToRangeFilter
from django_filters.rest_framework import BaseInFilter, CharFilter, FilterSet

from car.models import Car
from order.models import Order

class DateFilter(FilterSet):
    created_at = DateFromToRangeFilter()

    class Meta:
        model = Order
        fields = ['created_at']


class CarFilter(FilterSet):
    price = RangeFilter()

    class Meta:
        model = Car
        fields = ["price"]