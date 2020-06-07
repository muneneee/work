from django.contrib import admin
from .models import Project,Profile


admin.site.site_header = "Awards admin"
admin.site.site_title = "Awards admin area"
admin.site.index_title = "Welcome to Awards Admin"




admin.site.register(Project)
admin.site.register(Profile)
