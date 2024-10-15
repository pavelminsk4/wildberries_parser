import requests
from bs4 import BeautifulSoup
from celery import shared_task
from products.models import Product

@shared_task
def fetch_product_info(article):
    print('======>in_shared_task')
    url = f'https://www.wildberries.ru/catalog/{article}/detail.aspx'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)

    # # Здесь следует добавить логику для парсинга данных
    # stock = ...  # Логика получения остатка
    # warehouses = ...  # Логика получения складов
    # price = ...  # Логика получения цены

    Product.objects.update_or_create(
        article=article,
        price=129,
    )