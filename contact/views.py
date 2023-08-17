from django.shortcuts import render
from . models import ContactList, ContactUs

# Create your views here.


def contact_new(request):
    if request.method == 'POST':
        get_name = request.POST.get('name')
        get_email = request.POST.get('email')
        get_subject = request.POST.get('subject')
        get_message = request.POST.get('message')

        contact_us_data = ContactUs(name = get_name, email = get_email, subject = get_subject, message = get_message)
        contact_us_data.save()
    
    contactlist_data = ContactList.objects.all()[0]
    context ={
        'contact' :contactlist_data,
    }
    return render(request, 'contact.html', context) 