from rest_framework import serializers
from account.models import CustomUser
from .models import AccessoriesType, Brand, Category, Product, ProductHaveImages, ProductHaveColor


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

    def get_url(self, obj):
        return obj.get_absolute_url()
    


class ProductHaveColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductHaveColor
        fields='__all__'


    def get_url(self, obj):
        return obj.get_absolute_url()
    


class ProductHaveImagesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductHaveImages
        fields='__all__'

    def get_url(self, obj):
        return obj.get_absolute_url()
    


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields ='__all__'

    def get_url(self, obj):
        return obj.get_absolute_url()

