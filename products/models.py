from django.db import models
from base.models import BaseModel


class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null = True, blank = True)
    category_image = models.ImageField(upload_to = "category")

class Products(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null = True, blank = True)
    category = models.ForeignKey(Category ,related_name="products", on_delete=models.CASCADE)
    price = models.IntegerField()
    product_description = models.TextField()

class ProductImage(BaseModel):
    product = models.ForeignKey(Products, related_name="products", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product")