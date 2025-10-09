from django.urls import path, include
from rest_framework import routers

from order.views import OrderViewSet, SaleViewSet, OfferView

router = routers.SimpleRouter()
router.register(r"order", OrderViewSet)
router.register(r"sale", SaleViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("offer/", OfferView.as_view())
]
