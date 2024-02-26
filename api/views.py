from django.http import HttpResponse
from django.db.models.functions import Lower

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app import models
from . import serializers

def index(request):
    return HttpResponse('<h1>Welcome to the API HomePage</h1>')

@api_view(['GET'])
def get_app(request):
    
    ctx = {'app': {
        'context': {
            'name': 'iso14001',
            'info': 'json containing all instances of both the project and the region database tables'},
        'data': {}}}
    
    for project in models.Project.objects.all():
        
        try:
            project_data = {
                'project': serializers.ProjectSerializer(project).data,
                'actions': {}}
            
            try:
                actions = models.Action.objects.filter(project=project)
            
                for action in actions:
                    try:
                        actions = models.Action.objects.filter(name = action)[0]
                        action_data = serializers.ActionSerializer(actions).data
                        indicators = models.Indicator.objects.filter(action = action)
                        ind_data = serializers.IndicatorSerializer(indicators, many = True).data
                        action_data['actions'] = action_data
                        project_data['actions'][f'{action.ccaa}-{action.province}'] = ind_data
                        
                    except models.Indicator.DoesNotExist:
                        return Response(
                            data=f"No actions found for region with id {action.pk}",
                            status = status.HTTP_404_NOT_FOUND)
            
            except models.Action.DoesNotExist:
                return Response(
                    data = f"Region with id {action.pk} doesn't exist",
                    status = status.HTTP_404_NOT_FOUND)
            
            ctx['app']['data'][project.name] = project_data

        except models.Project.DoesNotExist:
            return Response(
                data=f"Project with the id {project.pk} doesn't exist",
                status = status.HTTP_404_NOT_FOUND)
    
    return Response(ctx)

@api_view(['GET'])
def get_full_project(request, slug):
    try:
        project = models.Project.objects.filter(slug = slug)[0]
        project_data = {
            'project': serializers.ProjectSerializer(project).data,
            'actions':{}}
        
        try:
            actions = models.Action.objects.filter(project = project)
            
            for action in actions:
                action_data = serializers.ActionSerializer(action).data
                
                try:
                    indicators = models.Indicator.objects.filter(action = action)
                    indicators_data = serializers.IndicatorSerializer(indicators, many = True).data
                    
                    action_data['indicators'] = indicators_data
                    project_data['actions'][f'{action.ccaa}-{action.province}'] = action_data
                    
                except models.Indicator.DoesNotExist:
                    return Response(
                        data = f"Indicators not found in action with id {action.pk}",
                        status = status.HTTP_404_NOT_FOUND)
                
        except models.Action.DoesNotExist:
            return Response(
                data = f"Action with id {action.pk} doesn't exist",
                status = status.HTTP_404_NOT_FOUND)
            
    except models.Project.DoesNotExist:
        return Response(
            data = f"Project with id {project.pk} doesn't exist",
            status = status.HTTP_404_NOT_FOUND)
        
    return Response(project_data)

@api_view(['GET'])
def fetch_project_list(request):
    
    start = int(request.GET.get('start', 0))
    end = start + 15
    project_list = models.Project.objects.all()[start:end]
    project_data = serializers.ProjectSerializer(project_list, many = True).data
    
    return Response(project_data)

@api_view(['GET'])
def filter_project_list(request):
    
    slug = request.GET.get('slug')
    projects = models.Project.objects.filter(slug__contains = slug)
    projects_data = serializers.ProjectSerializer(projects, many = True).data
    
    return Response(projects_data)

@api_view(['GET'])
def fetch_project_names(request):
    
    name = request.GET.get('name')
    
    project_filtered = models.Project.objects.filter(name__icontains=name)
    project_names = project_filtered.values_list('name', flat=True)
    
    return Response(project_names)