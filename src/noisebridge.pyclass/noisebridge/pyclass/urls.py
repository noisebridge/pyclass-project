from django.conf.urls.defaults import patterns, include, url
from pyclass.profiles import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'pyclass.views.index'),
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),

    # Sets up default URLs for django-registration
    #url(r'^accounts/', include('registration.backends.default.urls')),

    #Simplified registration (no email sent)
    url(r'^accounts/', include('registration.backends.simple.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
