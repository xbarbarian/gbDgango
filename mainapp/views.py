from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView
from django.views.generic.detail import SingleObjectMixin

from mainapp.models import Product, ProductCategory


# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'mainapp/index.html', context)


# def products(request, category_id=None, page=1):
#     context = {
#         'title': 'GeekShop - Каталог',
#         # 'products': Product.objects.all(),
#         'categories': ProductCategory.objects.all()
#     }
#     if category_id:
#         products = Product.objects.filter(category_id=category_id)
#         # context.update({'products': Product.objects.filter(category_id=category_id)})
#     else:
#         products = Product.objects.all()
#         # context.update({'products': Product.objects.all()})
#
#     paginator = Paginator(products, per_page=3)
#     products_paginator = paginator.page(page)
#
#     context.update({'products': products_paginator})
#     return render(request, 'mainapp/products.html', context)


# def single_product(request, id):
#     context = {
#         'product': Product.objects.get(id=id)
#     }
#     return render(request, 'mainapp/product.html', context)


class ProductListView(ListView):
    paginate_by = 2
    model = Product
    template_name = 'mainapp/products.html'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Каталог'
        context['category'] = Product.objects.all()
        return context


class ProductCategoryListView(ListView):
    model = Product
    template_name = 'mainapp/products.html'
