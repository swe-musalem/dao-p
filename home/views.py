from django.shortcuts import render
# Create your views here.
from django.contrib.auth.models import User
from users.models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
def home(request):
    return render(request,'home/home.html')

@login_required
def companys(requset):
    companys = Ads.objects.all()
    print(companys)
    context = {
        'companys':companys
    }
    return render(requset,'companys/companys.html',context)
@login_required
def students(request):
    students = Profile.objects.filter(is_company=False)
    context = {
        'students':students
    }
    return render(request,'student/student.html',context)


@login_required
def addCompanyAd(request):
    user = request.user
    profile = Profile.objects.filter(user=user)
    print(profile)
    if profile.filter(is_company=True):
        if request.method == "POST":
            companyName =  request.POST.get('companyname')
            spec =  request.POST.get('spec')
            seats = request.POST.get('seats')
            gpa =  request.POST.get('gpa')
            
            ads = Ads(companyName = companyName, spec=spec, seats=seats , gpa=gpa, companyLink=user)
            ads.save()

        return render(request,'companys/addco.html')
    return HttpResponse("unauth")