from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request): # for looking at progress
    return render(request, 'home.html')

def training_options(request):
    return render(request, 'training_options.html')

def groups_view(request):
    return render(request, 'groups.html')

def leaderboard_view(request):
    return render(request, 'leaderboards.html')