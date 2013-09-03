from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    # local apps
    url(r'^', include('website.urls', namespace='website')),

    # external apps
    url(r'^selectable/', include('selectable.urls')),

    # django apps
    url(r'^admin/', include(admin.site.urls)),

)
