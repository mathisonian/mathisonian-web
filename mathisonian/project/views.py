from django.template import RequestContext
from django.shortcuts import render_to_response
from mathisonian.project.models import Project


def home(request):
    projects = Project.objects.all().order_by('-created_at')
    return render_to_response('projects.jade',
                            {'projects': projects},
                            context_instance=RequestContext(request))
