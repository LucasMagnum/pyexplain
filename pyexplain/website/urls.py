import views
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^explain/$', views.ExplainView.as_view(), name='explain'),
)
