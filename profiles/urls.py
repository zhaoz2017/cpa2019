from django.urls import path, include
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', views.profile_page, name="info"),
    path('create', views.profile_create, name="create"),
]
