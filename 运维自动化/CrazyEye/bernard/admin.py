from django.contrib import admin
from bernard import models
# Register your models here.


class SchedulLogAdmin(admin.ModelAdmin):
    list_display = ('plan','status','start_date','end_date')


class StageAdmin(admin.ModelAdmin):
    list_display = ("id","name")

#admin.site.register(models.Schedule)
admin.site.register(models.Plan)
admin.site.register(models.Stage,StageAdmin)
admin.site.register(models.Job)
admin.site.register(models.SCPTask)
admin.site.register(models.SSHTask)
admin.site.register(models.ScheduleLog,SchedulLogAdmin)