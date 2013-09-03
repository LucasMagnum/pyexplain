import views
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^explain/$', views.ExplainView.as_view(), name='explain'),
    url(r'^keyword/(?P<codname>\w+)/$', views.KeywordDetail.as_view(), name='keyword_detail'),

    url(r'^category/$', views.CategoryList.as_view(), name='category_list'),
    url(r'^category/(?P<name>\w+)/$', views.CategoryDetail.as_view(), name='category_detail'),

    url(r'^favicon\.ico$', 'django.views.generic.RedirectView',
        {'url': '/static/website/favicon.ico'}),
)
