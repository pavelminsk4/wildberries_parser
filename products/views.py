from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product
from shtutgart.tasks import get_card_info
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ViewSet):
    def create(self, request):
        article = request.data.get('article')
        get_card_info.delay(article) # Запуск задачи
        return Response({'status': 'task started'})

    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
