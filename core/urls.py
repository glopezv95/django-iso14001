from django.contrib import admin
from django.urls import path, include

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    
    # APPS
    path('iso14001/', include('app.urls')),
    
    # REST API
    path('api/', include('api.urls')),
]
