from django.contrib import admin

from application.models import Group, ApplicationStatus, Application


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(ApplicationStatus)
class ApplicationStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    pass
