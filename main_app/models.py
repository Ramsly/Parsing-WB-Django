from django.db import models
from datetime import datetime


class Card(models.Model):
    article = models.IntegerField(default=0)
    title = models.CharField(default='', max_length=255, blank=True)
    price_without_disc = models.IntegerField(default=0, blank=True)
    price_with_disc = models.IntegerField(default=0, blank=True)
    brand = models.CharField(default='', max_length=255, blank=True)
    date = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return f'{self.title} - {self.article}'