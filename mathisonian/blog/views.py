from django.template import RequestContext
from django.shortcuts import render_to_response
from mathisonian.blog.models import Post
from mathisonian.blog.forms import PostForm

from django.shortcuts import get_object_or_404, redirect


def home(request):
    posts = Post.objects.all().order_by('-created_at')[:20]
    return render_to_response('weblog.jade',
                            {'posts': posts},
                            context_instance=RequestContext(request))


def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render_to_response('post.jade',
                            {'post': post},
                            context_instance=RequestContext(request))


def create_post(request):
    if request.method == 'POST' and request.POST['pw'] == 'fuckthisgayearth':

        form = PostForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/weblog/')

    else:
        form = PostForm()

    return render_to_response('create_post.jade',
                              {'form': form},
                              context_instance=RequestContext(request))
