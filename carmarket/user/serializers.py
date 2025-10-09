from rest_framework import serializers

from user.models import Buyer, Seller


class BuyerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = "__all__"


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = "__all__"
