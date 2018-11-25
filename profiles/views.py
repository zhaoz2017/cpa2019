from django.shortcuts import render
from .models import Profile
# from django.contrib.auth.decorators import login_required
# Create your views here.
def profile_page(request):
    profiles = Profile.objects
    return render(request, 'profiles/profile_page.html', {'profiles': profiles})

# @login_required(login_url="/account/login/")
def profile_create(request):
    return render(request, 'profiles/profile_create.html')
