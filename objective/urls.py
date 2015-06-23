from django.conf.urls import include, url
from django.contrib import admin
from objective.views import ApplicationView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^applications/$', ApplicationView.as_view(), name='applications')
]
