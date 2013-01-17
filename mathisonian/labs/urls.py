from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('mathisonian.labs.views',
    url(r'^$', r'home')
)
