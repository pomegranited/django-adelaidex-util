from django.conf.urls import patterns, url, include
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^/', include(admin.site.urls)),
)
