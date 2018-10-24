from django.urls import path, include
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.profile_list, name="info"),
]
