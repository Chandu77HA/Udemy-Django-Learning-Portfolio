from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def employee(request):
    return HttpResponse("This is employee Page")

def profile(request):
    return HttpResponse("This is employee-profile Page")

def profile_new(request):
    return render(request, 'employee/profile.html')