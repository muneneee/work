from django.contrib import admin
from .models import Project,Profile,Review,Choice


admin.site.site_header = "Awards admin"
admin.site.site_title = "Awards admin area"
admin.site.index_title = "Welcome to Awards Admin"





class ChoiceInline(admin.TabularInline):
    model = Choice
    extre = 5


class ReviewAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['criteria']}),('project',{'fields': ['project']})]
    inlines = [ChoiceInline] 




admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Review, ReviewAdmin)
