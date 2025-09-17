from django.db import models

from main.models import DefaultMixin


class Buyer(DefaultMixin):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    balance = models.FloatField(max_length=16)


class Seller(DefaultMixin):
    name = models.CharField(max_length=128)
    description = models.TextField()
    balance = models.FloatField(max_length=16)
