from django.urls import path

from authapp.views import LoginFormView, RegisterView, logout, ProfileView

app_name = 'authapp'

urlpatterns = [
    path('login/', LoginFormView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('logout/', logout, name='logout'),
    path('verify/<str:email>/<str:activation_key>/', RegisterView.verify, name='verify'),
]
