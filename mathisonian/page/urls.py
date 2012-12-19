from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('mathisonian.page.views',
    url(r'^about/?$', r'about')
)
