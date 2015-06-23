__author__ = 'joshbabier'

from django.conf.urls import url

from objective_app.views import ApplicationView

urlpatterns = [
    url(r'^$', ApplicationView.as_view(), name='applications')
]
