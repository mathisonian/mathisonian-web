from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.syndication.views import Feed


class Post(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.title)

        super(Post, self).save(*args, **kwargs)


    def __unicode__(self):
        return u'%s' % self.title



class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post)


class BlogFeed(Feed):
    title = "Mathisonian Weblog"
    link = "/weblog"
    description = "Just some ramblin's from mathisonian.com"

    def items(self):
        return Post.objects.order_by('-created_at')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return '/weblog/' + item.slug
