from django.db import models
from django_countries.fields import CountryField

class DefaultMixin:
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Brands(DefaultMixin, models.Model):
    name = models.CharField(max_length=100)


class Buyer(DefaultMixin, models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cash = models.DecimalField(max_digits=10, decimal_places=2)


class Showroom(DefaultMixin, models.Model):
    name = models.CharField(max_length=100)
    location = CountryField()
    cash = models.DecimalField(max_digits=10, decimal_places=2)
    brands = models.ManyToManyField(Brands, related_name='brands')


class CarsInShowroom(DefaultMixin, models.Model):
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, related_name='cars_in_showroom')
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE, related_name='showrooms')
    model = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


class Order(DefaultMixin, models.Model):
    buyer = models.ForeignKey(Buyer, related_name='buy',
                              on_delete=models.PROTECT)
    showroom = models.ForeignKey(Showroom, related_name='showroom',
                                 on_delete=models.PROTECT)


class Seller(DefaultMixin, models.Model):
    brand = models.ForeignKey(Brands, related_name='brand',
                              on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()


class CarInSeller(DefaultMixin, models.Model):
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, related_name='cars_in_seller')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='seller')
    model = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)