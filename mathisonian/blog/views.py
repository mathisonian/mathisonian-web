import os
from django.template import RequestContext
from django.shortcuts import render_to_response
from mathisonian.blog.models import Post
from mathisonian.blog.forms import PostForm
from django.core.paginator import Paginator

from django.shortcuts import get_object_or_404, redirect


def home(request, page=1):
    posts = Post.objects.all().order_by('-created_at')

    paginator = Paginator(posts, 4)

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)


    return render_to_response('weblog.jade',
                            {'posts': posts},
                            context_instance=RequestContext(request))


def post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    return render_to_response('post.jade',
                            {'post': post},
                            context_instance=RequestContext(request))


def create_post(request):
    if request.method == 'POST' and request.POST['pw'] == os.environ.get('MATHISONIAN_BLOG_PW'):

        form = PostForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/weblog/')

    else:
        form = PostForm()

    return render_to_response('create_post.jade',
                              {'form': form},
                              context_instance=RequestContext(request))
