from django.urls import path, include
from rest_framework import routers

from user.views import BuyerViewSet, SellerViewSet


router = routers.SimpleRouter()
router.register(r'buyer', BuyerViewSet)
router.register(r'seller', SellerViewSet)


urlpatterns = [
    path('', include(router.urls))
]