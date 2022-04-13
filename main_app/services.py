import requests
from bs4 import BeautifulSoup as Bs

from .models import Card

header = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
 Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36'
}


def get_html(url, header, params=None):
    response = requests.get(url=url, headers=header, params=params)
    html = response.text
    return html


def get_content(html):
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
