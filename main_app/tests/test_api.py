from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from main_app.serializers import CardSerializer
from main_app.models import Card


class CardApiTestCase(APITestCase):

    def test_api(self):
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
        url = reverse('cards')
        response = self.client.get(url)
        serializer_data = CardSerializer([card_1, card_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)