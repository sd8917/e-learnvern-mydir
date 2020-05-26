from django.shortcuts import render
from django.http import HttpResponse
from . models import Phone

# Create your views here.

def home(request):
    #if we make a post request means we are going to add something to the data base then 
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        print(name)
        print(number)

        p = Phone(name=name, number=number)
        p.save()

        return render(request, 'phone/home.html', {'message': 'Your phone number is added'})

    else:
        return render(request, 'phone/home.html')

def show(request):
    names = Phone.objects.all()

    return render(request, 'phone/show.html', {'names': names})
