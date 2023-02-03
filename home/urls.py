from django.urls import path
from django.contrib.auth import views as authentication_view
from . import views


app_name = "home"

urlpatterns = [
    path('',views.home,name="home"),
    path('companys/',views.companys,name="companys"),
    path('companys/add',views.addCompanyAd,name="add"),
    path('students/',views.students,name="student")
]