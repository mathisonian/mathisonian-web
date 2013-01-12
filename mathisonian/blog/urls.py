from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('mathisonian.blog.views',
    url(r'^$', r'home'),
    url(r'^(?P<post_id>\d+)/?$', r'post'),
    url(r'^create/?$', r'create_post')
)
