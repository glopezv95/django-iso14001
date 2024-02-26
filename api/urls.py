from django.urls import path
from rest_framework.routers import DefaultRouter

from api import views

app_name = 'api'

router = DefaultRouter()

urlpatterns = [
    path('', views.index, name = 'index'),
    path('iso14001/', views.get_app, name = 'iso14001'),
    path('iso14001/projects/<slug:slug>/', views.get_full_project, name = 'full_project'),
    path('iso14001/fetch-project-list/', views.fetch_project_list, name = 'fetch-project-list'),
    path('iso14001/fetch-project-names', views.fetch_project_names, name = 'fetch-project-names'),
]