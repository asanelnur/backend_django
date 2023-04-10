from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from products import models, serializers


# Create your views here.

class ProductAPIViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class CategoryAPIViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class CategoryProductsAPI(APIView):
    def get(self,request, *args, **kwargs):
        id = kwargs.get("id")
        lst = models.Product.objects.filter(category_id=id)
        return Response({'products': serializers.ProductSerializer(lst, many=True).data})
