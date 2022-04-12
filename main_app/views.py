from rest_framework import viewsets

from .models import Card
from .serializers import CardSerialization


class CardModelViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerialization