from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# Create your views here.
def semester_plan(request):
    return render(request, 'semplan/semester_plan.html')
