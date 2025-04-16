from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    profiles = ["Norman", "Sheila", "Anthony", "Gaby", "Julianna"]
    context = {
        'profiles': profiles,
    }
    return render(request, "home.html", context)