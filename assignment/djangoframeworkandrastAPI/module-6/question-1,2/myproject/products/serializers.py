from rest_framework import serializers
from .models import ProductMst, ProductSubCat

class ProductMstSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductMst
        fields = '__all__'

class ProductSubCatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSubCat
        fields = '__all__'
