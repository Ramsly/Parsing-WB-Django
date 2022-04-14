from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from .models import Card
from .serializers import CardSerializer
from .filters import TimeFilter


class CardModelViewSet(viewsets.ModelViewSet):
    """ModelViewSet для модели Card."""
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = TimeFilter
    filter_fields = ['article']
    ordering_fields = ['article']