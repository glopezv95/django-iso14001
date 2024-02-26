from django import forms

from . import models

class ProjectForm(forms.ModelForm):
    
    class Meta:
        model = models.Project
        exclude = ('slug',)

class RegionForm(forms.ModelForm):
    
    class Meta:
        model = models.Action
        fields = "__all__"
        
    def clean(self):
        
        clean_data = super().clean()
        
        start_date = clean_data['start_date']
        end_date = clean_data['end_date']
        
        if start_date > end_date:
            
            RegionForm.add_error(
                self,
                field='end_date',
                error = forms.ValidationError(
                    "Please verify that the end date is greater than the start date"))