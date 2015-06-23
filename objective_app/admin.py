__author__ = 'joshbabier'

from django.contrib import admin
from .models import Job, Applicant, Skill

admin.site.register(Job)
admin.site.register(Applicant)
admin.site.register(Skill)

