from django.conf.urls import patterns, url
from django_adelaidex.util.tests.views import HomeView

urlpatterns = patterns('',
    url(r'^/?', HomeView.as_view()),
)
