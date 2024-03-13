from django.contrib import admin
from .models import AccessoriesType, Category, Brand, Product, Color, ProductHaveImages


admin.site.register(AccessoriesType)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Color)
admin.site.register(ProductHaveImages)

