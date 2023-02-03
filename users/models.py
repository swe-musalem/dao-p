from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):

    def __str__(self) -> str:
        return self.user.username
    is_company = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=10,blank=False,default="0507674278")
    email = models.CharField(max_length=100,blank=False, default="")
    cv = models.FileField(upload_to="files/",default="")


class Ads(models.Model):
    companyName = models.CharField(max_length=100 , blank=False,default="")
    title = models.CharField(max_length=100 , blank=False)
    spec = models.CharField(max_length=100 , blank=False)
    seats = models.CharField(max_length=100 , blank=False)
    gpa =  models.CharField(max_length=100 , blank=False)
    companyLink = models.ForeignKey(User,on_delete=models.CASCADE,default=0)

    def __str__(self) -> str:
        return self.companyName