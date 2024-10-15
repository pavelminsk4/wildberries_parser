from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product
from shtutgart.tasks import fetch_product_info
from .serializers import ProductSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class ProductViewSet(viewsets.ViewSet):
    def create(self, request):
        print('--------_>')
        article = request.data.get('article')
        print(article, '=======>')
        fetch_product_info.delay(article)  # Запуск задачи
        print('======>task_started')
        return Response({'status': 'task started'})

    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
