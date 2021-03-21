from django.urls import path

from mainapp.views import products, single_product

app_name = 'mainapp'

urlpatterns = [
   path('', products, name='index'),
   path('<int:category_id>/', products, name='product'),
   path('<int:product_id>/', single_product, name='single_product'),
   path('page/<int:page>/', products, name='page'),

]
