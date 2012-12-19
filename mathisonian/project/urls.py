from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('mathisonian.project.views',
    url(r'^$', r'home')
)
