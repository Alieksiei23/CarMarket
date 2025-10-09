from django.db import models

from main.models import DefaultMixin
from authcore.models import User


class Car(DefaultMixin):
    model = models.CharField(max_length=128)
    description = models.TextField()
    price = models.FloatField(max_length=16)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="id_user")
