from django.urls import path

from mainapp.views import products, product

app_name = 'mainapp'

urlpatterns = [
   path('', products, name='index'),
   path('<int:id>/', product, name='product'),
   path('<int:id>/', products, name='category'),
]
