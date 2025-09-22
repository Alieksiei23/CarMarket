from django.db import models

from main.models import DefaultMixin
from authcore.models import User


class Buyer(DefaultMixin):
    username = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    balance = models.FloatField(max_length=16, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="id_buyer")


class Seller(DefaultMixin):
    username = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    description = models.TextField(blank=True)
    balance = models.FloatField(max_length=16, null=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="id_seller"
    )
