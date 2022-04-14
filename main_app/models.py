from django.db import models


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
    provider = models.CharField(default='', max_length=255, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.article}'