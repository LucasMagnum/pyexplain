# coding: utf-8

from . import views

from django.conf.urls import url


urlpatterns = [
    url(
        r'^create/(?P<app_label>\w+)/(?P<model>\w+)/(?P<obj_id>\d+)/$',
        views.ExampleCreateView.as_view(),
        name='create'
    ),
    url(
        r'^update/(?P<pk>\d+)/$',
        views.ExampleUpdateView.as_view(),
        name='update'
    ),
]
