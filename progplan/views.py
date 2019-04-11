from django.shortcuts import render

def progplan(request):
    return render(request, 'progplan/progplan.html')
