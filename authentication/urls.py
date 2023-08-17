from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.authlogin, name = "login"),
    path('registration/', views.authregister, name = "registration"),
    path('forget-password/', views.forgetpassword, name = "forget-password"),
    path('logout/', views.authlogout, name = "logout"),

]