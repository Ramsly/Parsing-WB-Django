import requests
from bs4 import BeautifulSoup as Bs

from fullstats_test.celery import app
from .models import Card
from fullstats_test.settings import HEADER


def get_html(url: str, params=None) -> str:
    """
    Возвращает html страницу строкой.

    Принимает параметры url: str, params.
    """
    response = requests.get(url=url, headers=HEADER, params=params)
    html = response.text
    return html


@app.task()
def parse():
    """
    Парсинг WB и запись в бд.

    Ничего не возвращает.
    """
    soup = Bs(get_html('https://www.wildberries.ru/catalog/8151147/detail.aspx'), 'html.parser')
    items = soup.find_all('div', class_='same-part-kt__info-wrap')
    info = []
    for item in items:
        info.append(
            {'price_with_disc': int(soup.find('span', class_='price-block__final-price')
                                    .get_text(strip=True)
                                    .replace("₽", "")
                                    .replace("\xa0", "")),

             'price_without_disc': int(soup.find('del', class_='price-block__old-price')
                                       .get_text(strip=True)
                                       .replace("₽", "")
                                       .replace("\xa0", "")),

             'brand': [i.span.text for i in soup.select('.same-part-kt__header')][0],
             'title': [i.text for i in soup.select('.same-part-kt__header span')][1],
             'article': int(soup.find('span', id='productNmId').get_text(strip=True)),
             # TODO: 'provider': soup.select_one('.tooltipster-content p')
             })
    for data in info:
        Card.objects.create(article=data['article'],
                            title=data['title'],
                            price_without_disc=data['price_without_disc'],
                            price_with_disc=data['price_with_disc'],
                            brand=data['brand'],
                            provider='Me')


# TODO: Add filters to drf
# TODO: Add tests
# TODO: Add read_only fields