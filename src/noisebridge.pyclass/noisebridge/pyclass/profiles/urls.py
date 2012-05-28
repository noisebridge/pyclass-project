from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView
from pyclass.profiles.models import Interest

urlpatterns = patterns('pyclass.profiles.views',
    #url(r'^$', 'pyclass.views.index'),
    url(r'^settings/$', 'update_settings', name="user_settings"),
    url(r'^add/interest/$', 'add_interests', name="add_interest"),
    url(r'^search/interests/$', 'search_interests', name="search_interests"),
    url(r'^reset_avatar/$', 'reset_avatar', name="reset_avatar"),
    url(r'^interest/(?P<pk>\d+)/$',
        DetailView.as_view(model=Interest, context_object_name="interest",),
        name="interest_details"
    ),
    url(r'^(?P<user_name>\w+)/$', 'display_profile'),
)
