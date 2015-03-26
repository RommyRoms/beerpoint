
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'beerpoint.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^beer/all/', 'beer_list.views.choose_all_beers', name='choose_all_beers'),
    url(r'^beer/get/(?P<beer_id>\d+)/$', 'beer_list.views.detail_beer', name='detail_beer'),
    url(r'^$', 'beer_list.views.choose_all_beers', name='choose_all_beers'),

)

