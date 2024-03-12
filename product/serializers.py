from rest_framework import serializers
from django.core.exceptions import ValidationError
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
        lookup_field = 'slug'

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
    product_images = serializers.ListField(child=serializers.ImageField(max_length=None, use_url=True))
    product_colors = serializers.ListField(child=serializers.CharField(max_length=32))

    class Meta:
        model = Product
        fields ='__all__'

    def create(self, validated_data):
        product_images_data = validated_data.pop('product_images', [])
        product_colors_data = validated_data.pop('product_colors', [])
        product_instance = Product.objects.create(**validated_data)

        for product_image_data in product_images_data:
            try:
                ProductHaveImages.objects.create(product=product_instance, image=product_image_data)
            except ValidationError as e:
                raise serializers.ValidationError({'product_images': e.message})

        for product_color_data in product_colors_data:
            try:
                color_instance, created = ProductHaveColor.objects.get_or_create(name=product_color_data)
                product_instance.product_colors.add(color_instance)
            except ValidationError as e:
                raise serializers.ValidationError({'product_colors': e.message})

        return product_instance

    def get_url(self, obj):
        return obj.get_absolute_url()

