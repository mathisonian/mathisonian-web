from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import os
from mathisonian.blog.models import BlogFeed

PROJECT_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), os.path.pardir))

urlpatterns = patterns('',
    url(r'', include('mathisonian.base.urls')),
    url(r'^weblog/', include('mathisonian.blog.urls')),
    url(r'^portfolio/', include('mathisonian.project.urls')),
    url(r'^labs/', include('mathisonian.labs.urls')),
    url(r'', include('mathisonian.page.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls))
)


# Enable RSS!!!
feeds = {'blog': BlogFeed}

# if settings.LOCAL:
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    (r'^feeds/weblog/?$', BlogFeed()),
)
