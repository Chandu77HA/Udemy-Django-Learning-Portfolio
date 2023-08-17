from django.contrib import admin
from . models import ContactList, ContactUs

# Register your models here.

admin.site.register(ContactList)
admin.site.register(ContactUs)
