import requests
from bs4 import BeautifulSoup as Bs

from fullstats_test.celery import app
from .models import Card
from fullstats_test.settings import HEADER


def get_html(url: str, params=None) -> str:
    """
    Return html page as str

    :param str url: website url
    :param params:
    """
    response = requests.get(url=url, headers=HEADER, params=params)
    html = response.text
    return html


@app.task()
def parse():
    """
    Ничего не принимает

    Парсинг WB и запись в бд.

    Ничего не возвращает.
    """
    for card in Card.objects.all().distinct('article'):
        soup = Bs(get_html(f'https://www.wildberries.ru/catalog/{card.article}/detail.aspx'), 'html.parser')
        items = soup.find_all('div', class_='same-part-kt__info-wrap')
        info = []
        for item in items:
            price_without_disc = item.find('del', class_='price-block__old-price')
            if not price_without_disc:
                price_without_disc = 0
            else:
                price_without_disc = int(price_without_disc.get_text(strip=True).replace("₽", "").replace("\xa0", ""))
            info.append(
                {'price_with_disc': int(item.find('span', class_='price-block__final-price')
                                        .get_text(strip=True)
                                        .replace("₽", "")
                                        .replace("\xa0", "")),

                 'price_without_disc': price_without_disc,

                 'brand': [i.span.text for i in soup.select('.same-part-kt__header')][0],
                 'title': [i.text for i in soup.select('.same-part-kt__header span')][1],
                 'article': int(soup.find('span', id='productNmId').get_text(strip=True)),
                 })
        for data in info:
            Card.objects.create(article=data['article'],
                                title=data['title'],
                                price_without_disc=data['price_without_disc'],
                                price_with_disc=data['price_with_disc'],
                                brand=data['brand'])