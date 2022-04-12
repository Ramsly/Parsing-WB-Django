from rest_framework import viewsets

from .models import Card
from .serializers import CardSerializer


class CardModelViewSet(viewsets.ModelViewSet):
    """ModelViewSet для модели Card."""
    queryset = Card.objects.all()
    serializer_class = CardSerializer