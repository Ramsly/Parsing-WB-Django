import requests
from bs4 import BeautifulSoup as Bs

from fullstats_test.celery import app
from .models import Card
from fullstats_test.settings import HEADER


def get_html(url, params=None):  # TODO: Delete this func and convert to one
    response = requests.get(url=url, headers=HEADER, params=params)
    html = response.text
    return html


@app.task
def parse(html):
    soup = Bs(html, 'html.parser')
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
