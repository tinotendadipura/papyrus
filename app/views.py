from django.shortcuts import render , redirect , get_object_or_404,redirect
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request , 'index.html')

def shop(request):
    return render(request , 'shop/index.html')

def events(request):
    return render(request , 'events/index.html')

def blog(request):
    return render(request , 'blog/index.html')

def about(request):
    return render(request , 'about-us/index.html')

def team(request):
    return render(request , 'our-team/index.html')

def partiners(request):
    return render(request , 'partiners/index.html')


def contact(request):
    return render(request , 'get-in-touch/index.html')


def shop(request):
    return render(request , 'shop/index.html')

def our_story(request):
    return render(request , 'shop/index.html')

def food_gallary(request):
    return render(request , 'shop/index.html')