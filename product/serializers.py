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
    product_images = ProductHaveImagesSerializer(many=True)
    product_colors = ProductHaveColorSerializer(many=True)

    class Meta:
        model = Product
        fields ='__all__'

    def create(self,validated_data):
        product_images = validated_data.pop('product_images', [])
        product_colors = validated_data.pop('product_colors', [])
        product_instance = Product.objects.create(**validated_data)
        for product_image in product_images:
            ProductHaveImages.objects.create(product=product_instance,**product_image)
        
        for product_color in product_colors:
            color_name = product_color.get('name')
            try:
                    color_instance = ProductHaveColor.objects.get(name=color_name)
            except ProductHaveColor.DoesNotExist:
                    color_instance = ProductHaveColor.objects.create(name=color_name)
            product_instance.product_colors.add(color_instance)
        
        
        return product_instance
    

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        # Update other fields similarly...

        product_images_data = validated_data.get('product_images')
        if product_images_data:
            instance.product_images.all().delete()
            for product_image_data in product_images_data:
                ProductHaveImages.objects.create(product=instance, **product_image_data)

        product_colors_data = validated_data.get('product_colors')
        if product_colors_data:
            instance.product_colors.clear()
            for product_color_data in product_colors_data:
                color_name = product_color_data.get('name')
                try:
                    color_instance = ProductHaveColor.objects.get(name=color_name)
                except ProductHaveColor.DoesNotExist:
                    color_instance = ProductHaveColor.objects.create(name=color_name)
                instance.product_colors.add(color_instance)

        instance.save()
        return instance

    def get_url(self, obj):
        return obj.get_absolute_url()

