from django.conf.urls import patterns, url
from autoscale1 import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
)
