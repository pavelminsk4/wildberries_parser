import requests
from celery import shared_task
from products.models import Product


@shared_task
def get_card_info(article):
    baskets = ['01', '02', '03', '04', '05', '06', '07', '08', '09',
               '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    headers = {
        'sec-ch-ua-platform': '"macOS"',
        'Referer': f'https://www.wildberries.ru/catalog/{article}/detail.aspx?targetUrl=SG',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
    }
    for basket in baskets:
        try:
            url = f'https://basket-{str(basket)}.wbbasket.ru/vol{
                article[:4]}/part{article[:6]}/{article}/info/ru/card.json'
            response = requests.get(url, headers=headers)
            data = response.json()
            Product.objects.update_or_create(
                article=article,
                description=data['description'],
                vendor_code=data['vendor_code'],
                imt_name=data['imt_name'],
                contents=data['contents'],
                slug=data['slug']
            )
            return data
        except:
            None
