from django.test import TestCase

from main_app.serializers import CardSerializer
from main_app.models import Card


class CardTestCase(TestCase):

    def test_serializer(self):
        card_1 = Card.objects.create(article=523452,
                                     title='Кроссовки',
                                     price_without_disc=9000,
                                     price_with_disc=6000,
                                     brand='adidas')
        card_2 = Card.objects.create(article=5214243,
                                     title='Телефон',
                                     price_without_disc=72000,
                                     price_with_disc=0,
                                     brand='iphone')
        serializer_data = CardSerializer([card_1, card_2], many=True).data
        expected_data = [
            {
                'id': card_1.id,
                'article': 523452,
                'title': 'Кроссовки',
                'price_without_disc': 9000,
                'price_with_disc': 6000,
                'brand': 'adidas',
            },
            {
                'id': card_2.id,
                'article': 5214243,
                'title': 'Телефон',
                'price_without_disc': 72000,
                'price_with_disc': 0,
                'brand': 'iphone',
            },
        ]
        self.assertEqual(expected_data, serializer_data)