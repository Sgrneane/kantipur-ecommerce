from rest_framework import serializers
from django.core.exceptions import ValidationError
from account.models import CustomUser
from .models import AccessoriesType, Brand, Category, Product, ProductHaveImages, Color


class AccessoriesTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = AccessoriesType
        fields = '__all__'

    def get_url(self, obj):
        return obj.get_absolute_url()


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'

    def get_url(self, obj):
        return obj.get_absolute_url()

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
        lookup_field = 'slug'

    def get_url(self, obj):
        return obj.get_absolute_url()
    


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model=Color

    def get_url(self, obj):
        return obj.get_absolute_url()
    


class ProductHaveImagesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductHaveImages
        fields='__all__'

    def get_url(self, obj):
        return obj.get_absolute_url()
    


class ProductRetrieveSerializer(serializers.ModelSerializer):
    product_images = ProductHaveImagesSerializer(many=True,read_only=True)
    class Meta:
        model = Product
        fields ='__all__'

    def get_url(self, obj):
        return obj.get_absolute_url()
    

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude  = ['colors']

    def get_url(self, obj):
        return obj.get_absolute_url()

