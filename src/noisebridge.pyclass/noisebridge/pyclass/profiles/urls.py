from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('pyclass.profiles.views',
    #url(r'^$', 'pyclass.views.index'),
    url(r'^(?P<user_name>\w+)/$', 'display_profile'),
    url(r'^add/interest/$', 'add_interests'),
    url(r'^add/interest/interest_submitted/$', 'interest_submitted'),
    url(r'^display_avatar/$', 'display_avatar'),
    url(r'^search/interests/$', 'search_interests'),
)
