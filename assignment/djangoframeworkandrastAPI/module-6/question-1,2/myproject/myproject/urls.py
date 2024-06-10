from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import ProductMstViewSet, ProductSubCatViewSet

router = DefaultRouter()
router.register(r'products', ProductMstViewSet)
router.register(r'product_subcategories', ProductSubCatViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
