from django.shortcuts import render
from django.http import HttpResponse
from .models import MyModel
from .forms import MyForm

# Create your views here.


def home(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MyForm()
    return render(request, "index-app.html", {"form": form})

def login(request):
    return render(request, "login.html")


def services(request):
    return render(request, "services.html")


def contacts(request):
    return render(request, 'contacts.html')

    
    return render(request,"index-app.html")