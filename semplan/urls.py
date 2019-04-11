from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.semester_plan, name="search"),
    path(r'^semester_planning', views.main, name="semester_plan")
    #path('test/', views.)
]
