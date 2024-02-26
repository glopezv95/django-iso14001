from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import forms
from . import models

def home(request):
    return render(request, 'index.html')

def iso14001_home(request):
    return render(request, 'app/index.html')

def project_home(request):
    
    if request.method == 'POST':
        
        data = request.POST
        p = forms.ProjectForm(data)
            
        if p.is_valid():
            
            p.save()
            slug = models.Project.objects.get(name=p.cleaned_data['name']).slug
            
            redirect_url = reverse('app:region_form', kwargs={'slug':slug})
            return HttpResponseRedirect(redirect_url)
            
    else:    
        p = forms.ProjectForm()
    
    projects = models.Project.objects.all()
    num_projects = len(projects)
    num_pages = int(num_projects/20)
    
    ctx = {
        'projects': projects,
        'project_form': p,
        'num_projects': num_projects,
        'num_pages': num_pages,
    }
    return render(request, 'app/project_index.html', ctx)

def region_home(request):
    return render(request, 'app/region_index.html')

def region_form(request, slug):
    
    project = models.Project.objects.filter(slug=slug)[0]
    project_name = project.name
    
    if request.method == 'POST':
        
        data = request.POST
        r = forms.RegionForm(data)
            
        if r.is_valid():
            r.save()
            return HttpResponseRedirect(request.path)
        else:
            print(r.errors)
            
    else:    
        r = forms.RegionForm()
        
    ctx = {
        'region': r,
        'project_name': project_name,
    }
        
    return render(request, 'app/region_form.html', ctx)

def action_home(request,project_slug, region_slug):
    pass