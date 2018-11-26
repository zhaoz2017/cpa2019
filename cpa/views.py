from django.http import HttpResponse
from django.shortcuts import render
from profiles.models import Profile

def homepage(request):
    #return HttpResponse('homepage')
    profiles = Profile.objects
    return render(request, 'homepage.html', {'profiles': profiles})

def about(request):
    #return HttpResponse('about')
    return render(request, 'about.html')
