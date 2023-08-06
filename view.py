from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"index.html") 

def aboutus(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")

def pricing(request):
    return render(request,"pricing.html")

def car(request):
    return render(request,"car.html")

def blog(request):
    return render(request,"blog.html")

def contact(request):
    return render(request,"contact.html")