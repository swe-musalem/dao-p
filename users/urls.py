from . import views
from django.urls import path
from django.contrib.auth import views as authentication_view


app_name = 'users'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',authentication_view.LoginView.as_view(template_name='login.html'),name='login'),
    path('registerCo/',views.registerCompany,name='registerCo'),
    path('logout/',authentication_view.LogoutView.as_view(template_name='home/home.html'),name='logout'),
]

