from django.contrib import admin
from .models import (
Expertise,
Skill,
Volunteer,
)
# Register your models here.
admin.site.register(Expertise)
admin.site.register(Skill)
admin.site.register(Volunteer)
