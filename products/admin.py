from django.contrib import admin
from .models import *

admin.site.register(Category)

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]

admin.site.register(Products, ProductAdmin)

admin.site.register(ProductImage)
