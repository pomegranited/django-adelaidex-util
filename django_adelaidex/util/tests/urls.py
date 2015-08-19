from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django_adelaidex.util.tests.views import HomeView

urlpatterns = patterns('',
    url(r'^/?', HomeView.as_view(), name='home'),
)
urlpatterns += staticfiles_urlpatterns()
