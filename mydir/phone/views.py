from django.shortcuts import render
from django.http import HttpResponse
from . models import Phone

# Create your views here.

def home(request):
    return render(request, 'phone/home.html')


def show(request):
    names = Phone.objects.all()

    return render(request, 'phone/show.html', {'names': names})
