from django.shortcuts import render
import json

from mainapp.models import Product, ProductCategory


# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request, id=None):
    context = {
        'title': 'GeekShop - Каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }

    return render(request, 'mainapp/products.html', context)


def product(request):
    context = {
        'title': Product.name
    }
    return render(request, 'mainapp/product.html', context)


