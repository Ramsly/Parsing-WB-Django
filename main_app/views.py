from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Card
from .serializers import CardSerializer


class CardModelViewSet(viewsets.ModelViewSet):
    """ModelViewSet для модели Card."""
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filter_fields = ['article', 'brand']
    ordering_fields = ['article', 'brand']