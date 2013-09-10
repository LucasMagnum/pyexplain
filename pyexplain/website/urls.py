import views
from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(
        r'^$',
        views.IndexView.as_view(),
        name='index'
    ),
    url(
        r'^explain/$',
        views.ExplainView.as_view(),
        name='explain'
    ),
    url(
        r'^category/$',
        views.CategoryList.as_view(),
        name='category_list'
    ),
    url(
        r'^category/(?P<slug>[\w_-]+)/$',
        views.CategoryDetail.as_view(),
        name='category_detail'
    ),
    url(
        r'^category/(?P<category_slug>[\w_-]+)/(?P<key_slug>[\w_-]+)/$',
        views.KeywordDetail.as_view(),
        name='keyword_detail'
    ),
)
