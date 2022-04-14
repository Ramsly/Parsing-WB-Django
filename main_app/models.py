from django.db import models
from datetime import datetime

from custom_user.models import CustomUser


class Card(models.Model):
    """
    Модель карточки товара.
    Поля: article, title, price_without_disc, price_with_disc, brand, provider.
    """
    article = models.IntegerField(default=0)
    title = models.CharField(default='', max_length=255, blank=True)
    price_without_disc = models.IntegerField(default=0, blank=True)
    price_with_disc = models.IntegerField(default=0, blank=True)
    brand = models.CharField(default='', max_length=255, blank=True)
    date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return f'{self.title} - {self.article}'