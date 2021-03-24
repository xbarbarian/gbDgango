from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView

from mainapp.models import Product, ProductCategory


# Create your views here.
def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'mainapp/index.html', context)


class ProductListView(ListView):
    paginate_by = 2
    model = Product
    template_name = 'mainapp/products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop - Каталог'
        context['categories'] = ProductCategory.objects.all()
        return context

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        queryset = super(ProductListView, self).get_queryset()
        return queryset.filter(category_id=category_id) if category_id else queryset



