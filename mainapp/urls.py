from django.urls import path

from mainapp.views import products

app_name = 'mainapp'

urlpatterns = [
   path('', products, name='index'),
   path('<str:id>/', products, name='product'),
   path('<int:pk>', products, name='category'),
]
