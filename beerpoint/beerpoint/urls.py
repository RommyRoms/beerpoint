from django.conf.urls import patterns, include, url
from django.contrib import admin




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'beerpoint.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('beer_list.urls', namespace='beer_list')),

)
