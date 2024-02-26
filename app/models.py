from django.db import models
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField
from django.utils.text import slugify

from .data.vars import ccaa_list, province_list

max_length_ccaa = max([len(i) for i in ccaa_list])
max_length_province = max([len(i) for i in province_list])

class Project(models.Model):

    name = models.CharField(_("Project name"), max_length=250)
    created_at = models.DateField(_("Date created"), auto_now=False, auto_now_add=True)
    updated_at = models.DateField(_("Publising date"), auto_now=True, auto_now_add=False)
    slug = models.SlugField(unique=True, editable=False, max_length = 50)

    def save(self, *args, **kwargs):
        
        if not self.slug:
            
            base_slug = slugify(self.name)[:45]
            self.slug = base_slug
            counter = 1
            
            while Project.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1
                
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return self.name
    
class Action(models.Model):
    
    project = models.ForeignKey("app.Project", verbose_name=_("Project name"), on_delete=models.CASCADE)
    name = models.CharField(_("Action Name"), max_length=250)
    ccaa = models.CharField(_("Autonomous Community"),
                            max_length=max_length_ccaa,
                            choices=[(v, v) for v in ccaa_list],
                            default =ccaa_list[0])
    
    province = models.CharField(_("Province"),
                                max_length=max_length_province,
                                choices=[(v, v) for v in province_list],
                                default = province_list[0])
    
    start_date = models.DateField(_("Start date"), auto_now=False, auto_now_add=False)
    est_end_date = models.DateField(_("Estimated end date"), auto_now=False, auto_now_add=False)
    end_date = models.DateField(_("End date"), auto_now=False, auto_now_add=False)
    responsible = models.CharField(_("Person responsible"), max_length=100)
    est_cost = MoneyField(_("Estimated cost"), max_digits=10, decimal_places=2, default_currency='EUR')
    est_benefit = MoneyField(_("Estimated benefit"), max_digits=10, decimal_places=2, default_currency='EUR')
    cost = MoneyField(_("Real cost"), max_digits=10, decimal_places=2, default_currency='EUR')
    benefit = MoneyField(_("Real benefit"), max_digits=10, decimal_places=2, default_currency='EUR')
    slug = models.SlugField(unique=True, editable=False, max_length = 50)

    def save(self, *args, **kwargs):
        
        if not self.slug:
            
            base_slug = slugify(self.name)[:45]
            self.slug = base_slug
            counter = 1
            
            while Action.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1
                
        super().save(*args, **kwargs)
        
    class Meta:
        verbose_name = _("Action")
        verbose_name_plural = _("Action")

    def __str__(self):
        return self.name
    
class Indicator(models.Model):

    action = models.ForeignKey("app.Action", verbose_name=_("Action"), on_delete=models.CASCADE)
    energy = models.DecimalField(_("Energy consumption (kWh)"), max_digits=5, decimal_places=2)
    ren_energy = models.DecimalField(_("Renewable energy consumption (kWh)"), max_digits=5, decimal_places=2)
    co2 = models.DecimalField(_("Greenhouse gas emission (tCO2e)"), max_digits=5, decimal_places=2)
    no2 = models.DecimalField(_("NO2 gas emission (t)"), max_digits=5, decimal_places=2)
    so2 = models.DecimalField(_("SO2 gas emission (t)"), max_digits=5, decimal_places=2)
    pm = models.DecimalField(_("Particulate matter emission (t)"), max_digits=5, decimal_places=2)
    water = models.DecimalField(_("Water consumption (m³)"), max_digits=5, decimal_places=2)
    waste = models.DecimalField(_("Waste generation (t)"), max_digits=5, decimal_places=2)
    hazard = models.DecimalField(_("Hazardous waste generation (t)"), max_digits=5, decimal_places=2)
    land = models.DecimalField(_("Land use (m²)"), max_digits=5, decimal_places=2)
    train_h = models.DecimalField(_("Employee environmental training hours"), max_digits=5, decimal_places=2)
    incidents = models.IntegerField(_("Number of environmental incidents"))
    expenditures = models.IntegerField(_("Number of environmental expenditures"))

    class Meta:
        verbose_name = _("Indicator")
        verbose_name_plural = _("Indicators")

    def __str__(self):
        return f'{self.action}. Action {self.pk}'