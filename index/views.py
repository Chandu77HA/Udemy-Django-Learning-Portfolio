from django.shortcuts import render
from django.shortcuts import render
from .models import About, Slider, Client

def home_new(request):
    slider_data = Slider.objects.all()
    client_data = Client.objects.all()
    context = {
        'slider' : slider_data,
        'client' : client_data,
    }
    return render(request, 'home_new.html', context)

def about_new(request):
    about_data = About.objects.all()[1]
    context = {
        'about' : about_data
    }
    return render(request, 'about.html', context)



