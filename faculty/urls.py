# from django.urls import path, include
# from . import views
from django.urls import path, include
from . import views
from django.conf.urls import url
from django.contrib import admin
urlpatterns = [
    path('', views.faculty_page, name='faculties'),
    path('shome', views.shome, name='shome'),
    path('create', views.create, name='create'),
    path('<int:solution_id>', views.detail, name='detail'),
    path('<int:solution_id>/upvote', views.upvote, name='upvote'),
]
