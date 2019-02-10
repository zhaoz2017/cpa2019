from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Solution
from django.utils import timezone
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

def home(request):
    solutions = Solution.objects
    return render(request, 'faculty/home.html',{'solutions':solutions})

@login_required(login_url="/account/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body_q'] and request.POST['body_a']:
            solution = Solution()
            solution.title = request.POST['title']
            solution.body_q = request.POST['body_q']
            solution.body_a = request.POST['body_a']
            solution.pub_date = timezone.datetime.now()
            solution.publisher = request.user
            solution.save()
            return redirect('/faculty/' + str(solution.id))
        else:
            return render(request, 'faculty/create.html',{'error':'All fields are required.'})
    else:
        return render(request, 'faculty/create.html')

def detail(request, solution_id):
    solution = get_object_or_404(Solution, pk=solution_id)
    return render(request, 'faculty/detail.html',{'solution':solution})

@login_required(login_url="/account/signup")
def upvote(request, solution_id):
    if request.method == 'POST':
        solution = get_object_or_404(Solution, pk=solution_id)
        solution.votes_total += 1
        solution.save()
        return redirect('/faculty/' + str(solution.id))
