from rest_framework import viewsets
from .models import ProductMst, ProductSubCat
from .serializers import ProductMstSerializer, ProductSubCatSerializer

class ProductMstViewSet(viewsets.ModelViewSet):
    queryset = ProductMst.objects.all()
    serializer_class = ProductMstSerializer

class ProductSubCatViewSet(viewsets.ModelViewSet):
    queryset = ProductSubCat.objects.all()
    serializer_class = ProductSubCatSerializer
