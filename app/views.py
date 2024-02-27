from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import forms
from . import models

def format_num(num_list:list):

    formatted_nums = []
    
    for num in num_list:
        formatted_num = num[::-1]
        
        for i in range(len(formatted_num)):
            if i % 3 == 0 and i != 0:
                formatted_num = num[::-1][:i] + ' ' + num[::-1][i:]
        
        formatted_nums.append(formatted_num[::-1])
        
    return formatted_nums

def home(request):
    return render(request, 'index.html')

def iso14001_home(request):
    
    num_projects = str(models.Project.objects.count())
    num_actions = str(models.Action.objects.count())
    num_indicator_sets = str(models.Indicator.objects.count())
    
    
    num_ccaa = models.Action.objects.values('ccaa').distinct().count()
    num_provinces = models.Action.objects.values('province').distinct().count()
    
    indicators_list = [field.name for field in models.Indicator._meta.get_fields()]
    num_indicators = len(indicators_list)
    
    formatted_nums = format_num([num_projects, num_actions, num_indicator_sets])
    
    ctx = {
        'num_projects': formatted_nums[0],
        'num_actions': formatted_nums[1],
        'num_indicator_sets': formatted_nums[2],
        'num_ccaa': num_ccaa,
        'num_provinces': num_provinces,
        'indicators_list': indicators_list,
        'num_indicators': num_indicators,
    }
    
    return render(request, 'app/index.html', ctx)

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