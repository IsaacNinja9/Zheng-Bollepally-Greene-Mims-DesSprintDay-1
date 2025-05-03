from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request): # for looking at progress
    return HttpResponse('Home page')

def training_options(request):
    return HttpResponse('Options for Gym Training')