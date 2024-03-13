from typing import Iterable
from django.db import models
from django.urls import reverse
from account.models import CustomUser
import uuid
from datetime import datetime
from django.utils.text import slugify
# Create your models here.

#Class to store accessories type(EX:Smart phones,Tablets,Smart watches, earphones..etc)
class AccessoriesType(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    name = models.CharField(max_length = 256,null=False)
    slug = models.SlugField(max_length=300,unique=True,blank=True)
    description =  models.CharField(max_length = 200,null=True)


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('accessory-detail', kwargs={'slug': self.slug})

#Class to store brand information
class Brand(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    name = models.CharField(max_length = 200,null=False)
    accessories = models.ManyToManyField(AccessoriesType)
    slug = models.SlugField(max_length=300,unique=True,blank=True)
    image = models.ImageField(upload_to='media/products/Brand',default=None)
    description =  models.CharField(max_length = 2000, null=True)



    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('Brand-detail', kwargs={'slug': self.slug})
    
#Class to store product category(Eg: Apple ipad pro 12.9,iphone,Xioami X2,..)
class Category(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    name = models.CharField(max_length = 200,null=False)
    slug = models.SlugField(max_length=300,unique=True,blank=True)
    image = models.ImageField(upload_to='media/products/category',default=None, null=True)
    description =  models.CharField(max_length = 2000,null=True)



    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('categories', kwargs={'slug': self.slug})


#model to store product color
class Color(models.Model):
    name = models.CharField(max_length=32,unique=True)
    color_code =  models.CharField(max_length=16,null=True)


class ColorManager(models.Manager):
     def get_or_create_colors(self, colors):
        colors = [Color.objects.get_or_create(name=color)[0] for color in colors]
        return colors

#Class to store product
class Product(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True) 
    name = models.CharField(max_length=1000,null=False)
    slug = models.SlugField(unique = True,blank=True)
    quantity = models.PositiveIntegerField(default=0)
    discount = models.DecimalField(default=0,max_digits=10, decimal_places=2)
    size = models.CharField(max_length=32,null=True)
    is_publish = models.BooleanField(default = False)
    thumbnail_image = models.ImageField(upload_to='media/products/thumbnail_images',blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    accessory_type = models.ForeignKey(AccessoriesType,related_name='product_types',on_delete=models.SET_NULL,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,related_name = "products",on_delete = models.SET_NULL,null = True)
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    updated_date = models.DateTimeField(auto_now=True,null=True)
    objects = models.Manager()
    colors = models.ManyToManyField(Color,related_name='products')
    color_manager = ColorManager()
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)+'-'+str(self.public_id)[1:5] + str(self.public_id)[-1:-5]
        super().save(*args, **kwargs)
    
    def save_colors(self, colors):
        colors = Product.color_manager.get_or_create_colors(colors)
        self.colors.set(colors)

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug': self.slug})


#Class to store product images
class ProductHaveImages(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    product = models.ForeignKey(Product,related_name = "product_images",on_delete = models.CASCADE)
    image = models.ImageField(upload_to="media/products/product_images")

    def __str__(self):
        return str(self.product.name) + ":" + str(self.id)
