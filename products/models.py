from django.db import models
from base.models import BaseModel
from django.utils.text import slugify


class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null = True, blank = True)
    category_image = models.ImageField(upload_to = "category")
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.category_name
    

class ColorVariant(BaseModel):
    color_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    
    def __str__(self)->str:
        return self.color_name

class SizeVariant(BaseModel):
    size_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self)->str:
        return self.size_name
    


class Products(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null = True, blank = True)
    category = models.ForeignKey(Category ,related_name="products", on_delete=models.CASCADE)
    price = models.IntegerField()
    product_description = models.TextField()
    color_name = models.ManyToManyField(ColorVariant, blank=True)
    size_name = models.ManyToManyField(SizeVariant,blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Products, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.product_name


class ProductImage(BaseModel):
    product = models.ForeignKey(Products, related_name="products", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product")