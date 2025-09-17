from django.urls import path, include
from rest_framework import routers

from car.views import CarViewSet

router = routers.SimpleRouter()
router.register(r'', CarViewSet)

urlpatterns = [
    path('', include(router.urls))
]