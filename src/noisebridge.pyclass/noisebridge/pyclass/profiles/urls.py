from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('pyclass.profiles.views',
    #url(r'^$', 'pyclass.views.index'),
    url(r'^search/$', 'search_interests'),

) 