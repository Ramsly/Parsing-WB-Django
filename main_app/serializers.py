from rest_framework import serializers

from .models import Card


class CardSerializer(serializers.ModelSerializer):
    """Сериализация для модели Card."""
    class Meta:
        model = Card
        read_only_fields = ['title', 'price_without_disc', 'price_with_disc', 'brand', 'provider']