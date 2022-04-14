from rest_framework import serializers

from .models import Card


class CardSerializer(serializers.ModelSerializer):
    """Сериализация для модели Card."""
    class Meta:
        model = Card
        fields = '__all__'