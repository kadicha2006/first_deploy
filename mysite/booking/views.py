from rest_framework import viewsets, permissions
from .serializers import HotelSerializers
from .models import Hotel
from django_filters.rest_framework import DjangoFilterBackend

class HotelViewSets(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city', 'country']
    permission_classes = [permissions.IsAuthenticated]
