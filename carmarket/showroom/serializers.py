from rest_framework import serializers

from showroom.models import Showroom, Sale


class ShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showroom
        fields = ["username", "balance", "email"]


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = "__all__"
