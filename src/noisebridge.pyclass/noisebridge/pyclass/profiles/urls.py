from django.conf.urls.defaults import patterns, url
from django.views.generic import DetailView
from pyclass.profiles.models import Interest

urlpatterns = patterns('pyclass.profiles.views',
    #url(r'^$', 'pyclass.views.index'),
    url(r'^(?P<user_name>\w+)/$', 'display_profile'),
    url(r'^interest/(?P<pk>\d+)/$',
        DetailView.as_view(model=Interest, context_object_name="interest",),
        name="interest_details"
    ),
    url(r'^add/interest/$', 'add_interests'),
    url(r'^search/interests/$', 'search_interests'),
)
