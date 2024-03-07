from django.contrib import admin
from .models import AccessoriesType, Category, Brand, Product, ProductHaveColor, ProductHaveImages


admin.site.register(AccessoriesType)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(ProductHaveColor)
admin.site.register(ProductHaveImages)

