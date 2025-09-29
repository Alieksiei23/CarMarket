from django.db.models import Sum
from rest_framework import serializers

from showroom.models import Showroom
from order.models import Order


class ShowroomReportSerializer(serializers.ModelSerializer):
    profit = serializers.SerializerMethodField()
    orders = serializers.SerializerMethodField()
    buyers_amount = serializers.SerializerMethodField()
    sellers = serializers.SerializerMethodField()

    class Meta:
        model = Showroom
        fields = [
            "id", "username", "email", "profit", "orders", "buyers_amount", "sellers"
        ]

    def get_profit(self, obj):
        orders = Order.objects.filter(showroom=obj)
        profit = 0
        for order in orders:
            if order.buyer:
                profit += order.price
            else:
                profit -= order.price
        return profit

    def get_orders(self, obj):
        return Order.objects.filter(showroom=obj).count()

    def get_buyers_amount(self, obj):
        return Order.objects.filter(showroom=obj).exclude(buyer__isnull=True).values('buyer').distinct().count()

    def get_sellers(self, obj):
        return obj.seller.count()
