from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'pyclass.views.index'),
    url(r'^profile/', include('pyclass.profiles.urls')),
    url(r'^todo/', include('pyclass.todo.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    # Sets up default URLs for django-registration
    #url(r'^accounts/', include('registration.backends.default.urls')),

    #Simplified registration (no email sent)
    url(r'^accounts/', include('registration.backends.simple.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
