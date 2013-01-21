from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import redirect


def home(request):
    return redirect('/labs/processing/')


def processing(request):
    return render_to_response('pjs.jade',
                            {},
                            context_instance=RequestContext(request))


def processing2d(request):
    return render_to_response('pjs-editor-2d.jade',
                            {},
                            context_instance=RequestContext(request))


def processing3d(request):
    return render_to_response('pjs-editor-3d.jade',
                            {},
                            context_instance=RequestContext(request))


def canvas(request):
    return render_to_response('processing/particles.pde',
                            {},
                            context_instance=RequestContext(request))
