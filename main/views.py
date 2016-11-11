
from django.shortcuts import render, get_object_or_404, redirect, render_to_response


# Create your views here.
def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def registration(request):
    return render(request, 'static/register/registration.html')


def services(request):
    return render(request, 'services.html')
