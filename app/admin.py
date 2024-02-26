from django.contrib import admin

from . import models

model_list = [
    models.Project,
    models.Action,
    models.Indicator,
]

for model in model_list:
    admin.site.register(model)