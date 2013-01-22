from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('mathisonian.labs.views',
    url(r'^$', r'home'),
    url(r'^processing/?$', r'processing'),
    url(r'^processing/2d/?$', r'processing2d'),
    url(r'^processing/3d/?$', r'processing3d'),
    url(r'^particles.pde$', r'canvas')
)
