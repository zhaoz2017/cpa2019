from django.shortcuts import render

# Create your views here.
def faculty_page(request):
    return render(request, 'faculty_page.html')
