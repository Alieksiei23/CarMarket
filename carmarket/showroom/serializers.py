from rest_framework import serializers

from showroom.models import Showroom


class ShowroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showroom
        # fields = "__all__"
        fields = ["username", "balance", "email", "seller", "user"]
