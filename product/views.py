from django.shortcuts import render
from django.db import transaction
import json
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import AccessoriesType, Brand, Category, Product, Color, ProductHaveImages
from .serializers import (AccessoriesTypeSerializer, BrandSerializer, CategorySerializer, ProductSerializer,ColorSerializer, ProductHaveImagesSerializer,
                         ProductRetrieveSerializer)
from .helpers import get_or_create_color, create_image

class AccessoriesTypeViewSet(viewsets.ModelViewSet):
    queryset = AccessoriesType.objects.all()
    serializer_class = AccessoriesTypeSerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    related_field = 'slug'

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductRetrieveSerializer

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ProductSerializer
        return super().get_serializer_class()
    
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance=serializer.save()
        images = create_image(request.data.getlist('product_images'),serializer.data['id'])
        colors_data = self.request.data.get('colors', [])
        colors_data = json.loads(colors_data)
        if len(colors_data) != 0:
            instance.save_colors(colors_data)
        else:
            pass
        headers = self.get_success_headers(serializer.data)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        # data = request.data.copy()
        # colors= data['colors']
        # print(data)
        # colors = json.loads(colors)
        # print(colors)
        # color_ids = get_or_create_color(colors)
        # data['colors'] =  color_ids
        # print(data['colors'])
        # serializer = self.get_serializer(data=data)
        # serializer.is_valid(raise_exception=True)
        # self.perform_create(serializer)
        # print(serializer.data)
        # images = create_image(request.data.getlist('product_images'),serializer.data['id'])
        # headers = self.get_success_headers(serializer.data)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data.copy()
        colors = data.pop('colors', [])  # Retrieve and remove colors from data
        color_ids = get_or_create_color(colors)
        data['colors'] = color_ids
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        images = create_image(request.data.get_list('product_images'), instance.id)
        return Response(serializer.data)
        

        
class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class ProductHaveImagesViewSet(viewsets.ModelViewSet):
    queryset = ProductHaveImages.objects.all()
    serializer_class = ProductHaveImagesSerializer

