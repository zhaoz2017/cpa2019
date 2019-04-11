from django.urls import path, include
from . import views
from django.conf.urls import url
from django.contrib import admin
urlpatterns = [
    path('', views.prog_page, name='plan')
]
