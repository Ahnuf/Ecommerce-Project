from django.shortcuts import render
from products.models import Products


def get_product(request, slug):
    try:
        product = Products.objects.get(slug=slug)
        return render(request, "product/product.html", context = {'product': product})

    except Exception as e:
        print(e)