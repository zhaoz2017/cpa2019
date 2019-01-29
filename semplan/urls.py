from django.urls import path, include
from . import views

app_name = 'semplan'

urlpatterns = [
    path('', views.semester_plan, name='semester_plan'),
]
