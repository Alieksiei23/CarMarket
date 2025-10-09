from django.urls import path, include
from rest_framework import routers

from showroom.views import ShowroomViewSet

router = routers.SimpleRouter()
router.register(r"", ShowroomViewSet)

urlpatterns = [path("", include(router.urls))]
