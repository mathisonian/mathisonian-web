from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('mathisonian.base.views',
    url(r'^$', r'home')
)
