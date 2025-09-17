from django.urls import path, include
from rest_framework import routers

from showroom.views import ShowroomViewSet, SaleViewSet

router = routers.SimpleRouter()
router.register(r'showroom', ShowroomViewSet)
router.register(r'sale', SaleViewSet)

urlpatterns = [
    path('', include(router.urls))
]