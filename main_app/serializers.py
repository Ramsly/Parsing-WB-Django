from rest_framework import serializers

from .models import Card


class CardSerializer(serializers.ModelSerializer):
    """Сериализация для модели Card."""
    class Meta:
        model = Card
        fields = ['id', 'article', 'title', 'price_without_disc', 'price_with_disc', 'brand', 'provider']
        read_only_fields = ['id', 'title', 'price_without_disc', 'price_with_disc', 'brand', 'provider']