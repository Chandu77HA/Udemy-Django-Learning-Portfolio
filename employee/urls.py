
from django.urls import path
from . import views

urlpatterns = [

    path('', views.employee, name = "employee"),
    path('profile/', views.profile, name = "profile"),
    path('profile_new/', views.profile_new, name = "profile_new"),


]