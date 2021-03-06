from django.conf.urls import patterns, include, url
from mysite.views import hello, current_datetime, time_plus, show_meta
from mysite.books import views 
from django.contrib import admin
admin.autodiscover

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^hello/$|^$', hello),
    url(r'^time/$', current_datetime),
    url(r'^timeplus1/$', time_plus, {'hours': 1}),
    url(r'^time/plus/(?P<hours>\d{1,2})/$', time_plus),
    url(r'^admin/$', include(admin.site.urls)),
    url(r'^meta/$', show_meta),
    url(r'^search-form/$', views.search),
    url(r'^search?/$', views.search),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
