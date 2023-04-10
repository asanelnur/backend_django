from django.urls import path, include
from rest_framework import routers
from products import views


app_name = 'products'

router = routers.SimpleRouter()
router.register(r'products', views.ProductAPIViewSet)
router.register(r'categories', views.CategoryAPIViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('categories/<int:id>/products', views.CategoryProductsAPI.as_view())
]
