from django.shortcuts import render
from .models import Course
from .models import Meeting
from django.core.paginator import Paginator
from django.db.models import Q

def main(request):
    return render(request, 'semplan/main.html')

def semester_plan(request):
    # Start by getting all courses by 1title (alphabetical)
    course = Course.objects.all().order_by('title')
    # Get Title Query Keyword
    title = request.GET.get('q')
    # Get Subject Query Keyword
    subject = request.GET.get('s')
    # Get Course Number Query Number
    number = request.GET.get('n')
    # Get Professor Query Keyword
    professor = request.GET.get('p')
    # Get Begin Time Query Time
    inbegin = request.GET.get('bt')
    # Get End Time Query Time
    inend = request.GET.get('et')
    time = request.GET.get('time')
    Mon = request.GET.get('M')
    Tue = request.GET.get('T')
    Wed = request.GET.get('W')
    Thu = request.GET.get('R')
    Fri = request.GET.get('F')
    Sat = request.GET.get('Sat')
    Sun = request.GET.get('U')
    eight = 800
    twelve = 1200
    five = 1700
    nine = 2100
    # Initialize as None; holds query results
    match = None
    list = None
    queryList = []
    # If there's a title search
    T,S,N,P,B,E,M,Tu,W,R,F,Sa,Su = None, None, None, None, None, None, None, None, None, None, None, None, None

    """if title:
        match = Meeting.objects.filter(crn__title=title)"""

    """if title and subject:
        match = Course.objects.filter(Q(title__icontains=title) & Q(sub__iexact=subject))
"""
    if title: # WORKS
        T = Q(title__icontains=title)
        queryList.append(T)
        # Get any objects where title contains the keyword
        # match = Course.objects.filter(T).values_list('crn','sub', 'num', 'title', 'section', 'prof', 'cred', 'sem','max_enroll','actual_enroll', 'meeting__building', 'meeting__room', 'meeting__begin_time', 'meeting__end_time', 'meeting__days')
    # If there's a subject search
    if subject: # WORKS
        S = Q(sub__iexact=subject)
        queryList.append(S)
        # Get any objects where the subject is exactly the keyword
        # match = Course.objects.filter(sub__iexact=subject).values_list('crn','sub', 'num', 'title', 'section', 'prof', 'cred', 'sem','max_enroll','actual_enroll', 'meeting__building', 'meeting__room', 'meeting__begin_time', 'meeting__end_time', 'meeting__days')
    if number: # WORKS
        N = Q(num__iexact=number)
        queryList.append(N)
        # Get objects where the number is exactly the number given
        #match = Course.objects.filter(num__iexact=number).values_list('crn','sub', 'num', 'title', 'section', 'prof', 'cred', 'sem','max_enroll','actual_enroll', 'meeting__building', 'meeting__room', 'meeting__begin_time', 'meeting__end_time', 'meeting__days')
    # If there's a professor search
    if professor: # WORKS
        P = Q(prof__iexact=professor)
        queryList.append(P)
        # Get any objects where the professor is exactly the keyword
        # match = Course.objects.filter(prof__iexact=professor).values_list('crn','sub', 'num', 'title', 'section', 'prof', 'cred', 'sem','max_enroll','actual_enroll', 'meeting__building', 'meeting__room', 'meeting__begin_time', 'meeting__end_time', 'meeting__days')
    if inbegin and inend: # WORKS
        B = Q(meeting__begin_time__gte=inbegin)
        E = Q(meeting__end_time__lte=inend)
        queryList.append(B)
        queryList.append(E)
        #match = Course.objects.filter(meeting__begin_time__gte=inbegin).filter(meeting__end_time__lte=inend).values_list('crn','sub', 'num', 'title', 'section', 'prof', 'cred', 'sem','max_enroll','actual_enroll', 'meeting__building', 'meeting__room', 'meeting__begin_time', 'meeting__end_time', 'meeting__days')
    elif time == "0": # PROBLEM
        morn = Q(meeting__begin_time__gte=eight) & Q(meeting__end_time__lte=twelve)
        queryList.append(morn)
    elif time == "1": # PROBLEM
        after = Q(meeting__begin_time__gte=twelve) & Q(meeting__end_time__lte=five)
        queryList.append(after)
    elif time == "2": # PROBLEM
        even = Q(meeting__begin_time__gte=five) & Q(meeting__end_time__lte=nine)
        queryList.append(even)
    if Mon:
        M = Q(meeting__days__icontains="M")
        queryList.append(M)
        #match = Course.objects.filter(meeting__days__icontains="M").values_list('crn','sub', 'num', 'title', 'section', 'prof', 'cred', 'sem','max_enroll','actual_enroll', 'meeting__building', 'meeting__room', 'meeting__begin_time', 'meeting__end_time', 'meeting__days')
    if Tue:
        Tu = Q(meeting__days__icontains="T")
        queryList.append(Tu)
        #match = Course.objects.filter(meeting__days__icontains="T").values_list('crn','sub', 'num', 'title', 'section', 'prof', 'cred', 'sem','max_enroll','actual_enroll', 'meeting__building', 'meeting__room', 'meeting__begin_time', 'meeting__end_time', 'meeting__days')
    if Wed:
        W = Q(meeting__days__icontains="W")
        queryList.append(W)
        #match = Course.objects.filter(meeting__days__icontains="W").values_list('crn','sub', 'num', 'title', 'section', 'prof', 'cred', 'sem','max_enroll','actual_enroll', 'meeting__building', 'meeting__room', 'meeting__begin_time', 'meeting__end_time', 'meeting__days')
    if Thu:
        R = Q(meeting__days__icontains="R")
        queryList.append(R)
        #match = Course.objects.filter(meeting__days__icontains="R").values_list('crn','sub', 'num', 'title', 'section', 'prof', 'cred', 'sem','max_enroll','actual_enroll', 'meeting__building', 'meeting__room', 'meeting__begin_time', 'meeting__end_time', 'meeting__days')
    if Fri:
        F = Q(meeting__days__icontains="F")
        queryList.append(F)
        #match = Course.objects.filter(meeting__days__icontains="F").values_list('crn','sub', 'num', 'title', 'section', 'prof', 'cred', 'sem','max_enroll','actual_enroll', 'meeting__building', 'meeting__room', 'meeting__begin_time', 'meeting__end_time', 'meeting__days')
    if Sat:
        Sa = Q(meeting__days__icontains="S")
        queryList.append(Sa)
        #match = Course.objects.filter(meeting__days__icontains="S").values_list('crn','sub', 'num', 'title', 'section', 'prof', 'cred', 'sem','max_enroll','actual_enroll', 'meeting__building', 'meeting__room', 'meeting__begin_time', 'meeting__end_time', 'meeting__days')
    if Sun:
        Su = Q(meeting__days__icontains="U")
        queryList.append(Su)
        #match = Course.objects.filter(meeting__days__icontains="U").values_list('crn','sub', 'num', 'title', 'section', 'prof', 'cred', 'sem','max_enroll','actual_enroll', 'meeting__building', 'meeting__room', 'meeting__begin_time', 'meeting__end_time', 'meeting__days')
    if queryList:
        print(queryList)
        query = queryList.pop()
        for item in queryList:
            query &= item
        match = Course.objects.filter(query).values_list('crn','sub', 'num', 'title', 'section', 'prof', 'cred', 'sem','max_enroll','actual_enroll', 'meeting__building', 'meeting__room', 'meeting__begin_time', 'meeting__end_time', 'meeting__days').order_by('title')
        #print(match)

    """
    # Match for classes that contain Monday meeting Days
    match = course.objects.filter(meeting__days__icontains='M').values_list('crn','sub', 'num', 'title', 'section', 'prof', 'cred', 'sem','max_enroll','actual_enroll', 'meeting__building', 'meeting__room', 'meeting__begin_time', 'meeting__end_time', 'meeting__days')

    # Match for classes that don't meet on Mondays
    match = course.objects.exclude(meeting__days__icontains='M').values_list('crn','sub', 'num', 'title', 'section', 'prof', 'cred', 'sem','max_enroll','actual_enroll', 'meeting__building', 'meeting__room', 'meeting__begin_time', 'meeting__end_time', 'meeting__days')
    """

    # If there's a course number search
    # Paginate the results (50 items per page)
    page = request.GET.get('page', 1)
    if match:
        paginator = Paginator(match, 50)
        try:
            list = paginator.page(page)
        except PageNotAnInteger:
            list = paginator.page(1)
        except EmptyPage:
            list = paginator.page(paginator.num_pages)
    # Else if there isn't a search paginate by alphabetical title (could be problem)
    """else:
        paginator = Paginator(course, 50)
        try:
            list = paginator.page(page)
        except PageNotAnInteger:
            list = paginator.page(1)
        except EmptyPage:
            list = paginator.page(paginator.num_pages)"""

    print(list)

    # Return the query list for html page
    return render(request, 'semplan/semester_plan.html', {'list' : list})
