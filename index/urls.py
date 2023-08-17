from django.urls import path
from . import views

urlpatterns = [

    path('home-new/', views.home_new, name = "home-new"),
    path('about-new/', views.about_new, name = "about-new"),


]