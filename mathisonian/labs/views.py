from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import redirect

from mathisonian.labs.models import Sketch
from mathisonian.labs.forms import Create, NewVersion
from django.utils import simplejson
from django.http import HttpResponse


def home(request):
    return redirect('/labs/processing/')


def processing(request):
    return render_to_response('pjs.jade',
                            {},
                            context_instance=RequestContext(request))


def processing2d(request, sketch_id=None, version_id=None):
    sketch = None
    version = None
    if sketch_id:
        sketch = Sketch.get_from_encoded_id_or_404(encoded_id=sketch_id)
        version = sketch.get_version_or_404(v=version_id)

    return render_to_response('pjs-editor-2d.jade',
                            {'version': version,
                             'sketch_id': sketch_id},
                            context_instance=RequestContext(request))


def processing3d(request, sketch_id=None, version_id=None):
    sketch = None
    version = None
    if sketch_id:
        sketch = Sketch.get_from_encoded_id_or_404(encoded_id=sketch_id)
        version = sketch.get_version_or_404(v=version_id)

    return render_to_response('pjs-editor-3d.jade',
                            {'version': version,
                             'sketch_id': sketch_id},
                            context_instance=RequestContext(request))


def save_3d_sketch(request):
    if request.method == 'POST':
        form = Create(request.POST)
        if form.is_valid():
            sketch = form.save()

            to_json = {
                "sketch_id": sketch.get_encoded_id()
            }
            return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')

    else:
        form = Create()

    return render_to_response('pjs-editor-3d.jade',
                            {'form': form},
                            context_instance=RequestContext(request))


def version_3d_sketch(request):
    if request.method == 'POST':
        form = NewVersion(request.POST)
        if form.is_valid():
            version = form.save()

            to_json = {
                "version_number": version.version_number
            }
            return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')

    else:
        form = Create()

    return render_to_response('pjs-editor-3d.jade',
                            {'form': form},
                            context_instance=RequestContext(request))


def save_2d_sketch(request):
    if request.method == 'POST':
        form = Create(request.POST)
        if form.is_valid():
            sketch = form.save()

            to_json = {
                "sketch_id": sketch.get_encoded_id()
            }
            return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')

    else:
        form = Create()

    return render_to_response('pjs-editor-2d.jade',
                            {'form': form},
                            context_instance=RequestContext(request))


def version_2d_sketch(request):
    if request.method == 'POST':
        form = NewVersion(request.POST)
        if form.is_valid():
            version = form.save()

            to_json = {
                "version_number": version.version_number
            }
            return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')

    else:
        form = Create()

    return render_to_response('pjs-editor-2d.jade',
                            {'form': form},
                            context_instance=RequestContext(request))


def canvas(request):
    return render_to_response('processing/particles.pde',
                            {},
                            context_instance=RequestContext(request))
