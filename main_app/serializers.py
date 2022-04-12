from rest_framework import serializers

from .models import Card


class CardSerialization(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'