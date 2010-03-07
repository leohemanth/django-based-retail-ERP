from django.conf.urls.defaults import *
from erp.views import search_form , search

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^erp/', include('erp.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),
     ('^search_form/$',search_form),
     ('^search/$',search),

    # Uncomment the next line to enable the admin:
     (r'^admin/(.*)', admin.site.root),
)
