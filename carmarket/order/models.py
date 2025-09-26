from django.db import models

from main.models import DefaultMixin
from user.models import Buyer, Seller
from showroom.models import Showroom


class Order(DefaultMixin):
    model = models.CharField(max_length=128)
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


class Sale(DefaultMixin):
    name = models.CharField(max_length=128)
    description = models.TextField()
    discount = models.FloatField(max_length=16)
    date_start = models.DateField()
    date_end = models.DateField()
    showroom = models.ForeignKey(
        Showroom, on_delete=models.CASCADE, related_name="to_showroom"
    )
    seller = models.ForeignKey(
        Seller, on_delete=models.CASCADE, related_name="from_seller"
    )