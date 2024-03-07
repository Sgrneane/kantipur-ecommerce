from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AccessoriesTypeViewSet, BrandViewSet, CategoryViewSet, ProductViewSet, ProductHaveColorViewSet, ProductHaveImagesViewSet

router = DefaultRouter()
router.register(r'accessories-types', AccessoriesTypeViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-colors', ProductHaveColorViewSet)
router.register(r'product-images', ProductHaveImagesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]