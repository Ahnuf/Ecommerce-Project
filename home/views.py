from django.shortcuts import render
from products.models import Products


def index(request):
    context = {'products' : Products.objects.all()}
    return render(request, 'home/index.html', context)