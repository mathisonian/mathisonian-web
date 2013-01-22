from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('mathisonian.base.views',
    url(r'^$', r'home'),
    url(r'^robots\.txt$', direct_to_template, {'template': 'robots.txt', 'mimetype': 'text/plain'})
)
