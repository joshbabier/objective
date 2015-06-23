__author__ = 'joshbabier'

from django.views.generic import TemplateView

from .models import Applicant, Job, Skill


class ApplicationView(TemplateView):
    template_name = 'applications.html'

    def get_context_data(self, **kwargs):
        jobs = Job.objects.all()
        num_applicants = Applicant.objects.all().count()
        num_unique_skills = len(Skill.objects.values_list('name', flat=True).distinct())

        return {
            'jobs': jobs,
            'num_applicants': num_applicants,
            'num_unique_skills': num_unique_skills
        }
