from django.db import models
from django_countries.fields import CountryField


class DefaultMixin(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Buyer(DefaultMixin):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    balance = models.DecimalField(max_digits=8, decimal_places=2)


class Seller(DefaultMixin):
    name = models.CharField(max_length=128)
    description = models.TextField()
    balance = models.DecimalField(max_digits=8, decimal_places=2)


class Showroom(DefaultMixin):
    name = models.CharField(max_length=128)
    location = CountryField()
    balance = models.DecimalField(max_digits=8, decimal_places=2)
    seller = models.ManyToManyField(Seller, related_name='brands')



class Car(DefaultMixin):
    model = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE,
                               related_name='seller_id', null=True)
    showroom = models.ForeignKey(Showroom, on_delete=models.CASCADE,
                                 related_name='showroom_id', null=True)



class Order(DefaultMixin):
    description = models.TextField()
    balance = models.DecimalField(max_digits=8, decimal_places=2)
    buyer = models.ForeignKey(Buyer, related_name='buyer',
                              on_delete=models.PROTECT, null=True)
    showroom = models.ForeignKey(Showroom, related_name='showroom',
                                 on_delete=models.PROTECT)
    seller = models.ForeignKey(Seller, related_name='seller',
                               on_delete=models.PROTECT, null=True)


class Sale(DefaultMixin):
    name = models.CharField(max_length=128)
    description = models.TextField()
    discount = models.DecimalField(max_digits=8, decimal_places=2)
    date_start = models.DateField()
    date_end = models.DateField()
    showroom = models.ForeignKey(Buyer, on_delete=models.CASCADE,
                              related_name='to_showroom')
    seller = models.ForeignKey(Buyer, on_delete=models.CASCADE,
                              related_name='from_seller')
