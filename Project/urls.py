from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^traffic/', include('traffic.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('traffic.urls'))
)
