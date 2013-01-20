from django.template import RequestContext
from django.shortcuts import render_to_response


def home(request):
    return render_to_response('labs-base.jade',
                            {},
                            context_instance=RequestContext(request))


def canvas(request):
    return render_to_response('processing/particles.pde',
                            {},
                            context_instance=RequestContext(request))
