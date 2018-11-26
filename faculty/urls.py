from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.faculty_page, name='faculties'),
]
