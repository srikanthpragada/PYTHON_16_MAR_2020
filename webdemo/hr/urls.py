from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path("home", views.home),
     path("topics", views.topics),
     path("countries",views.list_countries),
     path("jobs",views.list_jobs),
     path("addjob",views.add_job),
     path("discount",views.discount),
     path("ajax",views.ajax_demo),
     path("now",views.get_datetime),
]
