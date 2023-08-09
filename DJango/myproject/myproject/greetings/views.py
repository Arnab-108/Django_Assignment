from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Hello, World!")

def greet(request , username):
    return HttpResponse(f"Hello, {username}")

def farewell(request, username):
    return HttpResponse(f"Goodbye, {username}!")

