from django.db import models

from main.models import DefaultMixin
from user.models import Buyer, Seller
from showroom.models import Showroom


class Order(DefaultMixin):
    description = models.TextField()
    price = models.FloatField(max_length=16)
    buyer = models.ForeignKey(
        Buyer, related_name="buyer", on_delete=models.PROTECT, null=True
    )
    showroom = models.ForeignKey(
        Showroom, related_name="showroom", on_delete=models.PROTECT
    )
    seller = models.ForeignKey(
        Seller, related_name="seller", on_delete=models.PROTECT, null=True
    )
