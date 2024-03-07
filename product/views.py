from django.shortcuts import render
from rest_framework import viewsets
from .models import AccessoriesType, Brand, Category, Product, ProductHaveColor, ProductHaveImages
from .serializers import AccessoriesTypeSerializer, BrandSerializer, CategorySerializer, ProductSerializer, ProductHaveColorSerializer, ProductHaveImagesSerializer

class AccessoriesTypeViewSet(viewsets.ModelViewSet):
    queryset = AccessoriesType.objects.all()
    serializer_class = AccessoriesTypeSerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductHaveColorViewSet(viewsets.ModelViewSet):
    queryset = ProductHaveColor.objects.all()
    serializer_class = ProductHaveColorSerializer

class ProductHaveImagesViewSet(viewsets.ModelViewSet):
    queryset = ProductHaveImages.objects.all()
    serializer_class = ProductHaveImagesSerializer

