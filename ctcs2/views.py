from django.shortcuts import render, redirect
from .models import Ctcs2
# from django.contrib.auth.decorators import login_required
from .import forms

# Create your views here.
# @login_required(login_url="/account/login/")
def initial_page2(request):
    return render(request, 'ctcs2/courses.html')
