from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField


class User(AbstractUser):
    email = models.EmailField(unique=True)
    location = CountryField(max_length=2, blank=True)
    user_types = (
        (1, 'buyer'),
        (2, 'showroom'),
        (3, 'seller'),
    )
    user_type = models.PositiveSmallIntegerField(choices=user_types)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "user_type"]