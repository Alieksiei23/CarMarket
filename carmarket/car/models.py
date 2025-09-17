from django.db import models

from main.models import DefaultMixin
from showroom.models import Showroom
from user.models import Seller

class Car(DefaultMixin):
    model = models.CharField(max_length=128)
    description = models.TextField()
    price = models.FloatField(max_length=16)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE,
                               related_name='seller_id', null=True)
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE,
                                 related_name='showroom_id', null=True)

