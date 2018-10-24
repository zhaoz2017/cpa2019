from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def signup_view(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #log the user in
            #return redirect('about')
            return redirect('profiles:info')
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {'form': form})

def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('profiles:info')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form':form})
