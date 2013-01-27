from django.db import models
from django.template.defaultfilters import slugify
from django.http import Http404


class SketchManager(models.Manager):
    def create(self, content, parent=None):
        """ Automatically attach the first draft to a new post. """
        sketch = super(SketchManager, self).create(parent=parent)
        sketch.create_version(content=content)

        return sketch


class Sketch(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('Sketch', blank=True, null=True)
    current_version = models.ForeignKey('Version', blank=True, null=True, default=None, related_name="sketch_current_version")

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so create version 1
            self.slug = slugify(self.title)

        super(Sketch, self).save(*args, **kwargs)

    def create_version(self, content):
        version_number = 0

        if self.current_draft:
            version_number = self.current_version.version_number + 1

        version = Version(content=content, version_number=version_number, sketch=self)
        version.save()

        return version

    def get_versions(self):
        return Version.objects.filter(sketch=self).order_by("-version_number")

    def get_version(self, v=None):
        if v is None:
            return self.current_version

        return Version.objects.get(sketch=self, version_number=v)

    def get_version_or_404(self, v=None):
        try:
            return self.get_version(v=v)
        except Version.DoesNotExist:
            raise Http404


class Version(models.Model):
    content = models.TextField()
    version_number = models.IntegerField()
    sketch = models.ForeignKey(Sketch)
    date_created = models.DateTimeField(auto_now_add=True)

    def is_current_version(self):
        return self.sketch.current_version == self
