from django.db import models
from base.models import BaseModel


class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(upload = "category")

class Products(BaseModel):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category ,realated_name="products", on_delete=models.CASCADE)
    price = models.IntegerField((""))
    product_description = models.TextField()

class ProductImage(BaseModel):
    product = models.ForeignKey(Prodcut, related_name="products", on_delete=models.CASCADE)
    image = models.ImageField(upload="product")