from django.urls import path
from . import views

urlpatterns = [

    path('us/', views.contact_new, name = "contact-new"),

]