from django.contrib import admin
from volunteers.models import Project, Skill, Volunteer

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Volunteer)

