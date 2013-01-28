from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('mathisonian.labs.views',
    url(r'^$', r'home'),
    url(r'^processing/?$', r'processing'),
    url(r'^processing/2d/?$', r'processing2d'),
    url(r'^processing/3d/?$', r'processing3d'),
    url(r'^processing/create/3d/?$', r'save_3d_sketch'),
    url(r'^processing/version/3d/?$', r'version_3d_sketch'),
    url(r'^processing/create/2d/?$', r'save_2d_sketch'),
    url(r'^processing/version/2d/?$', r'version_2d_sketch'),
    url(r'^processing/3d/(?P<sketch_id>[\w]+)/?$', r'processing3d'),
    url(r'^processing/3d/(?P<sketch_id>[\w]+)/(?P<version_id>\d+)/?$', r'processing3d'),
    url(r'^processing/2d/(?P<sketch_id>[\w]+)/?$', r'processing2d'),
    url(r'^processing/2d/(?P<sketch_id>[\w]+)/(?P<version_id>\d+)/?$', r'processing2d'),
    url(r'^particles.pde$', r'canvas')
)
