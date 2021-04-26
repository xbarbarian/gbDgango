from django.urls import path

from authapp.views import LoginFormView, RegisterListView, logout, ProfileEdit

app_name = 'authapp'

urlpatterns = [
    path('login/', LoginFormView.as_view(), name='login'),
    path('register/', RegisterListView.as_view(), name='register'),
    path('profile/', ProfileEdit.as_view(), name='profile'),
    path('logout/', logout, name='logout'),
    path('verify/<str:email>/<str:activation_key>/', RegisterListView.verify, name='verify'),
]
