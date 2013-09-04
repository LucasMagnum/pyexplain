from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views import generic
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    # local apps
    url(r'^', include('website.urls', namespace='website')),

    # external apps
    url(r'^selectable/', include('selectable.urls')),

    # django apps
    url(r'^admin/', include(admin.site.urls)),

    # fav, robots e etcs
    url(r'^favicon\.ico$', generic.RedirectView.as_view(url='/static/website/favicon.ico')),

)

if settings.DEBUG:
 urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


