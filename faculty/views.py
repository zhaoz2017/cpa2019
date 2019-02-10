from django.shortcuts import render
import requests
import json

# Create your views here.
def faculty_page(request):
    response = requests.get('http://api.fit.edu/directory/v3/departments/13601/employees')
    data = response.json()
    return render(request, 'faculty/faculty_page.html', {
        'first_name': data['records'][0]['name']['first'],
        'last_name': data['records'][0]['name']['last'],
        'email': data['records'][0]['email'],
    })
