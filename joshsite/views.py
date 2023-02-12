from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("index-app.html")


def login(request):
    return HttpResponse("login.html")


def services(request):
    return HttpResponse("services.html")


def contacts(request):
    return HttpResponse('contacts.html')

