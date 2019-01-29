from django.urls import path, include
from . import views

# app_name = 'ctcs2'

urlpatterns = [
    path('', views.initial_page2, name='steptwo'),
    # path('submit/', views.submit, name="submit"),
    # path('success/', views.success, name="success"),
]
