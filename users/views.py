from django.shortcuts import render
from .forms import NewUserForm
from django.http import HttpResponse
from home import views 
from .models import Profile
# Create your views here.
from django.shortcuts import redirect
from django.urls import reverse


def register(request):
    form = NewUserForm()
    
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        email = request.POST.get('email')
        username = request.POST.get('username')
        number  = request.POST.get('phonenumber')
        
        user = request.user
        print(email)
        print(form.errors)

        if form.is_valid() :
                user = form.save()
                profile = Profile(user=user,phonenumber=number,is_company=False,email=email)
                profile.save()
                return redirect(reverse('home:student'))

    return render(request,'register.html',{"form":form})


def registerCompany(request):
    form = NewUserForm()
    
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        email = request.POST.get('email')
        username = request.POST.get('username')
        number  = request.POST.get('phonenumber')

        user = request.user
        print(email)
        print(form.errors)

        if form.is_valid() :
                user = form.save()
                profile = Profile(user=user,phonenumber=number,is_company=True)
                profile.save()
                return redirect(reverse('home:student'))
    return render(request,'registerCo.html',{"form":form})
