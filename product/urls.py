from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccessoriesTypeViewSet, BrandViewSet, CategoryViewSet, ProductViewSet, ColorViewSet, ProductHaveImagesViewSet

router = DefaultRouter()
router.register(r'accessories-types', AccessoriesTypeViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-colors', ColorViewSet)
router.register(r'product-images', ProductHaveImagesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]