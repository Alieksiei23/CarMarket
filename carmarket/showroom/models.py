from django.db import models
from django_countries.fields import CountryField

from main.models import DefaultMixin
from user.models import Seller


class Showroom(DefaultMixin):
    name = models.CharField(max_length=128)
    location = CountryField()
    balance = models.FloatField(max_length=16)
    seller = models.ManyToManyField(Seller, related_name='brands')


class Sale(DefaultMixin):
    name = models.CharField(max_length=128)
    description = models.TextField()
    discount = models.FloatField(max_length=16)
    date_start = models.DateField()
    date_end = models.DateField()
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE,
                              related_name='to_showroom')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE,
                              related_name='from_seller')