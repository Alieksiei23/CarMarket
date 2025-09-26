from rest_framework import viewsets

from main.permissions import IsOwnerOrReadOnly
from showroom.models import Showroom
from showroom.serializers import ShowroomSerializer


class ShowroomViewSet(viewsets.ModelViewSet):
    queryset = Showroom.objects.all()
    serializer_class = ShowroomSerializer
    # permission_classes = (IsOwnerOrReadOnly,)
