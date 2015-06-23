__author__ = 'joshbabier'


from django.db import models

class Job(models.Model):
    name = models.CharField(max_length=255)

    @property
    def num_skills(self):
        skills = 0
        for applicant in self.applicants.all():
            skills += applicant.num_skills
        return skills

    def __unicode__(self):
        return self.name


class Applicant(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    website = models.CharField(max_length=255, null=True)
    cover_letter = models.TextField(null=True)
    job = models.ForeignKey(Job, related_name='applicants')

    @property
    def num_skills(self):
        return self.skills.count()

    def __unicode__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=255)
    applicant = models.ForeignKey(Applicant, related_name='skills')

    def __unicode__(self):
        return self.name

