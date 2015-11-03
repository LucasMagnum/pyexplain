from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views import generic
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    # local apps
    url(r'^', include('website.urls', namespace='website')),
    url(r'^links/', include('attach.links.urls', namespace='links')),
    url(r'^examples/', include('attach.examples.urls', namespace='examples')),

    # external apps
    url(r'^selectable/', include('selectable.urls')),
    url(r'^social/', include('social.apps.django_app.urls', namespace='social')),

    # django apps
    url(r'^admin/', include(admin.site.urls)),

    # fav, robots e etcs
    url(r'^favicon\.ico$', generic.RedirectView.as_view(url='/static/website/favicon.ico')),

)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


def handler500(request):
    """500 error handler which includes ``request`` in the context.

    Templates: `500.html`
    Context: None
    """
    import sys
    import traceback
    from django.template import Context, loader
    from django.http import HttpResponseServerError

    t = loader.get_template('500.html')
    typo, value, tb = sys.exc_info()

    return HttpResponseServerError(t.render(Context({
        'exception_value': value,
        'DEBUG': settings.TEMPLATE_DEBUG,
        'value': typo,
        'tb': traceback.format_exception(typo, value, tb)})))
