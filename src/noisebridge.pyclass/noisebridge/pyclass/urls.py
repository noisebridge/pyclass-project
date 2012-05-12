from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from pyclass.profiles import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'pyclass.views.index'),
    url(r'^search/$', views.search_interests),
    url(r'^addinterest/$', views.add_interests),
    url(r'^addinterest/interest_submitted.html$', views.interest_submitted),
    url(r'^display_avatar$', views.display_avatar),

    # Sets up default URLs for django-registration
    #url(r'^accounts/', include('registration.backends.default.urls')),

    #Simplified registration (no email sent)
    url(r'^accounts/', include('registration.backends.simple.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
