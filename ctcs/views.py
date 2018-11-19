from django.shortcuts import render, redirect, HttpResponse
from .models import Ctcs
from django.contrib.auth.decorators import login_required
from .import forms

# Create your views here.
@login_required(login_url="/account/login/")
def initial_page(request):
    form = forms.RegInfo()
    return render(request, 'ctcs/initial_page.html', {'form':form})

def submit(request):
    if request.method=='POST':
        form = forms.RegInfo(request.POST)
        if form.is_valid():
            ctcs = form.save()
            return redirect('ctcs:success')

    return redirect('ctcs')

def success(request):
    return HttpResponse("success")
