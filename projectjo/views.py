from django.shortcuts import render 
from projectjo.models import students


# Create your views here.
def Homepage (request):
     return render (request,"homepage.html")
def Home (request):
    return render (request,"home.html")
def Register (request):
     if request.method == 'POST':
          name = request.POST.get ("name")
          email=request.POST.get ("email")
          phone= request.POST.get("phone")
          password=request.POST.get("password")
          abc= students(Name=name,Email=email,Phone=phone,Password=password)
          abc.save()
     return render (request,"register.html")
def Login (request):
     return render (request,"login.html")
def Profile (request):
     return render (request,"profile.html")
def Logout (request):
     return render (request,"logout.html")