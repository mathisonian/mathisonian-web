from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('mathisonian.blog.views',
    url(r'^$', r'home'),
    url(r'^create/?$', r'create_post'),
    url(r'^(?P<post_slug>[-\w]+)/?$', r'post')
)
