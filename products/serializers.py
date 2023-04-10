from rest_framework import serializers

from products import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = models.Category
        fields = '__all__'
