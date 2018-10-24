from django.shortcuts import render

# Create your views here.
def profile_list(request):
    return render(request, 'profiles/profile_list.html')
