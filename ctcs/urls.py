from django.urls import path, include
from . import views

app_name = 'ctcs'

urlpatterns = [
    path('', views.initial_page, name='initial_page'),
    path('submit/', views.submit, name="submit"),
    path('success/', views.success, name="success"),
]
