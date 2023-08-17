from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("<h1> This is our Home page </h1>")

def about(request):
    return HttpResponse("<h1> This is our About page</h1> ")

def contact(request):
    return HttpResponse("<h1> This is our Contact page </h1>")

def database(request):
    data = "Get all the data from the database"
    return HttpResponse(data)

def home_check(request):
    return render(request, 'index.html')


