from django.urls import path, include
from rest_framework import routers

from .views import (BuyerViewSet, SellerViewSet,
                    ShowroomViewSet, CarViewSet,
                    OrderViewSet, SaleViewSet)


router = routers.SimpleRouter()
router.register(r'buyer', BuyerViewSet)
router.register(r'seller', SellerViewSet)
router.register(r'showroom', ShowroomViewSet)
router.register(r'car', CarViewSet)
router.register(r'order', OrderViewSet)
router.register(r'sale', SaleViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls))
]