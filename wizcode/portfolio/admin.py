from django.contrib import admin
from .models import Contact, Project
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'message')
    search_fields = ['full_name', 'subject', 'email']

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'url', 'desc')
    search_fields = ['project_name', 'url', 'desc']

admin.site.register(Contact, ContactAdmin)
admin.site.register(Project, ProjectAdmin)
    
admin.site.site_header = "WizCode Page Administration"