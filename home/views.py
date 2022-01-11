from django.contrib import messages
from django.shortcuts import HttpResponse, render
from home.models import Contact
from django.contrib import messages


def home(request):
    return render(request, 'home/home.html')


def about(request):
    return render(request, 'home/about.html')


from home.models import Contact

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message =request.POST['content']
        contact=Contact(name=name, email=email, phone=phone, message=message)
        contact.save()
    return render(request, "home/contact.html")

