from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "index-app.html")

def login(request):
    return render(request, "login.html")


def services(request):
    return render(request, "services.html")


def contact(request):
    return render(request, "contacts.html")

