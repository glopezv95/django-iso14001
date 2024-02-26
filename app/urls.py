from django.urls import path

from app import views

app_name = 'app'

urlpatterns = [
    path("", views.iso14001_home, name = 'home'),
    path('projects/', views.project_home, name = 'project_home'),
    path('projects/regions/', views.region_home, name = 'region_home'),
    # path('projects/form/', views.project_form, name = 'project_form'),
    path('projects/<slug:slug>/form', views.region_form, name = 'region_form')
]
