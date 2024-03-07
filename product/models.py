from typing import Iterable
from django.db import models
from django.urls import reverse
from account.models import CustomUser
import uuid
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
    slug = models.SlugField(max_length=300,unique=True,blank=True)
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
    description =  models.CharField(max_length = 2000,null=True)


    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})


#Class to store product
class Product(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True) 
    name = models.CharField(max_length=255,null=False)
    title = models.CharField(max_length = 1000,null = True)
    slug = models.SlugField(unique = True,blank=True)
    quantity = models.PositiveIntegerField(default=0)
    discount = models.DecimalField(default=0,max_digits=10, decimal_places=2)
    size = models.CharField(max_length=32,null=True)
    is_publish = models.BooleanField(default = False)
    thumbnail_image = models.ImageField(upload_to='products/thumbnail_images')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    accessory_type = models.ForeignKey(AccessoriesType,related_name='product_types',on_delete=models.SET_NULL,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,related_name = "products",on_delete = models.SET_NULL,null = True)
    


    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)+'-'+str(self.public_id)[1:5] + str(self.public_id)[-1:-5]
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug': self.slug})



#Product Color description
class ProductHaveColor(models.Model):
    name = models.CharField(max_length=32)
    product = models.ManyToManyField(Product,related_name = 'product_color')

    def __str__(self):
        return str(self.name)

#Class to store product images
class ProductHaveImages(models.Model):
    public_id = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    product = models.ForeignKey(Product,related_name = "product_images",on_delete = models.CASCADE)
    image = models.ImageField(upload_to="products/images")

    def __str__(self):
        return str(self.product.name) + ":" + str(self.id)
