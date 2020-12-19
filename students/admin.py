from django.contrib import admin

from students import models

admin.site.register(models.studen)
admin.site.register(models.technologi)
admin.site.register(models.project)
admin.site.register(models.courses)
admin.site.register(models.milestone)