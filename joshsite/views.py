from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request,"index-app.html")


def login(request):
    return render(request, "login.html")


def services(request):
    return render(request, "services.html")


def contacts(request):
    return render(request, 'contacts.html')

