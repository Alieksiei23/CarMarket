from django.dispatch import receiver
from djoser.signals import user_registered

from showroom.models import Showroom
from user.models import Seller, Buyer


@receiver(user_registered, dispatch_uid="create_profile")
def create_profile(sender, user, request, **kwargs):
    data = request.data

    match data.get("user_type"):
        case 1:
            Buyer.objects.create(
                user=user,
                username=data["username"],
                email=data["email"],
                balance=data.get("balance", 0),
            )
        case 2:
            Showroom.objects.create(
                user=user,
                username=data["username"],
                email=data["email"],
                location=data.get("location", ""),
                balance=data.get("balance", 0),
            )
        case 3:
            Seller.objects.create(
                user=user,
                username=data["username"],
                email=data["email"],
                description=data.get("description", ""),
                balance=data.get("balance", 0),
            )
