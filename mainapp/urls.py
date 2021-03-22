from django.urls import path

# from mainapp.views import products, single_product
from mainapp.views import ProductListView, ProductCategoryListView

app_name = 'mainapp'

urlpatterns = [
   path('', ProductListView.as_view(), name='index'),
   path('<int:pk>/', ProductListView.as_view(), name='product'),
   # path('<int:product_id>/', single_product, name='single_product'),
   # path('page/<int:page>/', products, name='page'),

]
