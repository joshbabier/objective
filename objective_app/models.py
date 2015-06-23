__author__ = 'joshbabier'


from django.db import models

class Job(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    @property
    def rowspan(self):
        rowspan = 0
        for applicant in self.applicants.all():
            rowspan += applicant.rowspan
        return rowspan

    def __unicode__(self):
        return self.name


class Applicant(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(default='', blank=True)
    website = models.CharField(max_length=255, default='', blank=True)
    cover_letter = models.TextField(default='', blank=True)
    job = models.ForeignKey(Job, related_name='applicants')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    @property
    def rowspan(self):
        return self.skills.count() or 1

    def __unicode__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=255)
    applicant = models.ForeignKey(Applicant, related_name='skills')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.name

