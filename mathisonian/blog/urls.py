from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('mathisonian.blog.views',
    url(r'^$', r'home')
)
