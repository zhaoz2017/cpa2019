from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.faculty_page, name='faculties'),
    path('home', views.home, name='home'),
    path('create', views.create, name='create'),
    path('<int:solution_id>', views.detail, name='detail'),
    path('<int:solution_id>/upvote', views.upvote, name='upvote'),
]
