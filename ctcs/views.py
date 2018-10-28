from django.shortcuts import render
from .models import Ctcs
from django.contrib.auth.decorators import login_required
from .import forms

# Create your views here.
@login_required(login_url="/account/login/")
def initial_page(request):
    form = forms.RegTime()
    form1 = forms.Major()
    return render(request, 'ctcs/initial_page.html', {'form':form}, {'form1':form1})