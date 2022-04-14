from django.db import models


class Card(models.Model):
    """
    Модель карточки товара.
    Поля: article, title, price_without_disc, price_with_disc, brand, provider.
    """
    article = models.IntegerField(default=0)
    title = models.CharField(default='', max_length=255, blank=True, editable=False)
    price_without_disc = models.IntegerField(default=0, blank=True, editable=False)
    price_with_disc = models.IntegerField(default=0, blank=True, editable=False)
    brand = models.CharField(default='', max_length=255, blank=True, editable=False)
    provider = models.CharField(default='', max_length=255, blank=True, editable=False)
    date = models.DateField(auto_now_add=True, editable=False)

    def __str__(self):
        return f'{self.title} - {self.article}'